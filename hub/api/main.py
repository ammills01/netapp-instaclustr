import logging
import os
from contextlib import closing
import psycopg
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(title="Platform Demo Catalog",docs_url=None,redoc_url=None,openapi_url=None)
app.add_middleware(CORSMiddleware,allow_origins=[os.environ["PUBLIC_ORIGIN"]],
                   allow_credentials=False,allow_methods=["GET"],allow_headers=[])
log=logging.getLogger("hub")

def read_catalog():
    try:
        with closing(psycopg.connect(os.environ["DATABASE_URL"],sslmode="verify-full",
                     sslrootcert=os.environ["PGSSLROOTCERT"],connect_timeout=5,
                     options="-c statement_timeout=5000 -c default_transaction_read_only=on")) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT document, launches FROM platform_hub.public_catalog")
                row=cur.fetchone()
                if row is None:
                    raise HTTPException(503,"Catalog not initialized")
        doc, launches=row
        for p in doc["platforms"]:
            for t in p["tools"]:
                t.update(launches.get(p["slug"]+"/"+t["slug"],{}))
        for p in doc["projects"]:
            p.update(launches.get("projects/"+p["slug"],{}))
        return doc
    except (psycopg.Error,KeyError) as exc:
        log.warning("Catalog unavailable: %s",type(exc).__name__)
        raise HTTPException(503,"Catalog unavailable") from None

@app.get("/api/catalog")
def catalog():
    return read_catalog()

@app.get("/healthz")
def health():
    read_catalog()
    return {"status":"ok"}
