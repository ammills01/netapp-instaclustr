import os
import sys
from pathlib import Path
import psycopg
from psycopg.types.json import Jsonb

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from build_catalog import load_catalog

data=load_catalog()
with psycopg.connect(os.environ["DATABASE_URL"],sslmode="verify-full",
                     sslrootcert=os.environ["PGSSLROOTCERT"],connect_timeout=5) as conn:
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO platform_hub.catalog(singleton,document)
          VALUES(true,%s) ON CONFLICT(singleton) DO UPDATE
          SET document=excluded.document,updated_at=now()""",(Jsonb(data),))
        rows=[(p["slug"],t["slug"]) for p in data["platforms"] for t in p["tools"]]
        rows += [("projects",p["slug"]) for p in data["projects"]]
        cur.executemany("""INSERT INTO platform_hub.launches(group_slug,item_slug)
          VALUES(%s,%s) ON CONFLICT DO NOTHING""",rows)
print("Seeded public catalog and launch records")
