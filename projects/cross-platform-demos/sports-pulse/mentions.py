import hashlib
import json
import re
from confluent_kafka import Consumer, Producer
from kafka_config import config

STOP=set("a an the and or to of for in on with from at by is are was were as be after before over into out up down new says say report reports news latest more about this that it its their team teams game games".split())

def terms(title):
    return sorted({w for w in re.findall(r"[a-z][a-z0-9'-]{2,35}",title.lower()) if w not in STOP})

def main():
    consumer=Consumer({**config(),"group.id":"sports-mentions-v1","auto.offset.reset":"earliest","enable.auto.commit":False})
    producer=Producer({**config(),"enable.idempotence":True})
    consumer.subscribe(["sports.news.raw.v1"])
    try:
        while True:
            msg=consumer.poll(1)
            if msg is None: continue
            if msg.error(): raise RuntimeError("Kafka consumer error")
            event=json.loads(msg.value())
            errors=[]
            def ack(err,_):
                if err: errors.append(str(err))
            for term in terms(event["title"]):
                identity=hashlib.sha256((event["event_id"]+"|"+term).encode()).hexdigest()
                m={k:event[k] for k in ("event_id","sport","source","source_type","published_at","timestamp_basis")}
                m.update(mention_id=identity,term=term)
                producer.produce("sports.mentions.v1",key=event["sport"]+"|"+term,value=json.dumps(m),on_delivery=ack)
            if producer.flush(30) or errors: raise RuntimeError("Mention delivery failed")
            consumer.commit(message=msg,asynchronous=False)
    finally: consumer.close()

if __name__=="__main__": main()
