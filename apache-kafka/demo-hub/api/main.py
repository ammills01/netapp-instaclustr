import logging
import os
from contextlib import closing
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg
from psycopg.rows import dict_row

app = FastAPI(title="Demo Hub Catalog", docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(CORSMiddleware, allow_origins=[os.environ["PUBLIC_ORIGIN"]],
                   allow_credentials=False, allow_methods=["GET"], allow_headers=[])
log = logging.getLogger("catalog")

def connect():
    return psycopg.connect(os.environ["DATABASE_URL"], sslmode="verify-full",
        sslrootcert=os.environ["PGSSLROOTCERT"], connect_timeout=5,
        options="-c statement_timeout=5000 -c default_transaction_read_only=on", row_factory=dict_row)

@app.get("/api/catalog")
def catalog():
    try:
        with closing(connect()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM demo_hub.public_catalog ORDER BY sort_order, slug")
                return cur.fetchall()
    except (psycopg.Error, KeyError) as exc:
        log.warning("Catalog query failed: %s", type(exc).__name__)
        raise HTTPException(503, "Catalog temporarily unavailable") from None

@app.get("/healthz")
def health():
    try:
        with closing(connect()) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1 FROM demo_hub.public_catalog LIMIT 1")
        return {"status": "ok"}
    except (psycopg.Error, KeyError):
        raise HTTPException(503, "Catalog temporarily unavailable") from None
