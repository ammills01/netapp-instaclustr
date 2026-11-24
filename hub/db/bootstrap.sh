#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../.."
: "${PGHOST:?Set comma-separated certificate-matching PostgreSQL DNS hosts}"
: "${PGUSER:?Set migration user}"
: "${PGSSLROOTCERT:?Set PostgreSQL CA certificate path}"
export PGDATABASE="${PGDATABASE:-postgres}"
export PGPORT="${PGPORT:-5432}"
export PGSSLMODE=verify-full
export PGTARGETSESSIONATTRS=read-write
export PGCONNECT_TIMEOUT=5
# Use protected PGPASSFILE or injected PGPASSWORD.
psql -X -v ON_ERROR_STOP=1 -c "SELECT current_database(), pg_is_in_recovery(), current_setting('transaction_read_only');"
psql -X -v ON_ERROR_STOP=1 -f hub/db/001_schema.sql
export DATABASE_URL="${DATABASE_URL:-}"
python3 hub/db/seed.py
if [[ -n "${DEMO_READER_ROLE:-}" ]]; then
  psql -X -v ON_ERROR_STOP=1 -v reader_role="$DEMO_READER_ROLE" -f hub/db/002_grant_reader.sql
fi
psql -X -v ON_ERROR_STOP=1 -c "SELECT count(*) FROM platform_hub.launches;"
