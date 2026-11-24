#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLATFORM_ORDER = ["apache-kafka","apache-cassandra","postgresql","clickhouse","opensearch","cadence","mcp-gateway"]
PROJECT_ORDER = ["instaclustr-api","deployment","prometheus","grafana","cross-platform-demos"]

def load_catalog():
    def read(group, order):
        return [json.loads((ROOT/group/slug/"manifest.json").read_text(encoding="utf-8")) for slug in order]
    return {"schema_version":1,"platforms":read("platforms",PLATFORM_ORDER),"projects":read("projects",PROJECT_ORDER)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args = parser.parse_args()
    expected = json.dumps(load_catalog(),ensure_ascii=False,indent=2)+"\n"
    out = ROOT/"docs/catalog.json"
    if args.check:
        if out.read_text(encoding="utf-8") != expected:
            raise SystemExit("Catalog drift: run python3 hub/build_catalog.py")
        print("Catalog is up to date")
    else:
        out.write_text(expected,encoding="utf-8")
