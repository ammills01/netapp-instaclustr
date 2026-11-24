import argparse
import calendar
import hashlib
import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
import feedparser
import requests
from confluent_kafka import Producer
from kafka_config import config

ROOT=Path(__file__).resolve().parent
TOPIC="sports.news.raw.v1"
SPORTS={"american_football":["Playoff race and quarterback depth","Defense shines in divisional matchup"],
"soccer":["Transfer window and Champions League tactics","Goalkeeper saves decisive penalty"],
"cricket":["T20 selection and spin bowling","Test series batting partnership"],
"baseball":["Bullpen depth and pitching rotation","Home run powers extra innings"],
"basketball":["Playoff race and rookie minutes","Three-point shooting and defensive rotations"]}

def now():
    return datetime.now(timezone.utc).isoformat()

def event(sport,source,kind,identity,title,url,published=None):
    observed=now()
    digest=hashlib.sha256((sport+"|"+source+"|"+identity).encode()).hexdigest()
    return dict(event_id=digest,sport=sport,source=source,source_type=kind,title=title[:500],
                url=url,published_at=published or observed,observed_at=observed,
                timestamp_basis="published" if published else "observed")

def synthetic():
    for sport,titles in SPORTS.items():
        for i,title in enumerate(titles):
            yield event(sport,"Synthetic demo","synthetic",str(i),title,None)

def rss(feeds_path):
    for f in json.loads(feeds_path.read_text()):
        if not f.get("enabled"): continue
        try:
            if urlparse(f["url"]).scheme!="https": raise ValueError("HTTPS required")
            with requests.get(f["url"],timeout=(5,15),stream=True,headers={"User-Agent":"SportsPulseDemo/0.1"},allow_redirects=False) as response:
                if response.status_code!=200: raise ValueError("Unexpected status")
                chunks=[]; total=0
                for chunk in response.iter_content(65536):
                    total+=len(chunk)
                    if total>2_000_000: raise ValueError("Feed too large")
                    chunks.append(chunk)
            doc=feedparser.parse(b"".join(chunks),sanitize_html=True)
            for item in doc.entries[:100]:
                title=item.get("title","").strip()
                url=item.get("link","")
                if not title or urlparse(url).scheme not in ("http","https"): continue
                stamp=item.get("published_parsed") or item.get("updated_parsed")
                published=datetime.fromtimestamp(calendar.timegm(stamp),timezone.utc).isoformat() if stamp else None
                yield event(f["sport"],f["source"],"rss",item.get("id") or url,title,url,published)
        except (requests.RequestException,ValueError,KeyError) as exc:
            logging.warning("Feed failed: %s (%s)",f.get("source","unknown"),type(exc).__name__)

def main():
    p=argparse.ArgumentParser(); mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--synthetic",action="store_true");mode.add_argument("--rss",action="store_true")
    p.add_argument("--once",action="store_true");p.add_argument("--interval",type=int,default=180)
    p.add_argument("--feeds",type=Path,default=ROOT/"feeds.example.json");args=p.parse_args()
    producer=Producer({**config(),"enable.idempotence":True})
    while True:
        failures=[]
        def delivered(err,msg):
            if err: failures.append(str(err))
        for e in synthetic() if args.synthetic else rss(args.feeds):
            producer.produce(TOPIC,key=e["event_id"],value=json.dumps(e),on_delivery=delivered)
            producer.poll(0)
        if producer.flush(30) or failures: raise RuntimeError("Kafka delivery failed")
        if args.once: break
        time.sleep(max(120,args.interval))

if __name__=="__main__": main()
