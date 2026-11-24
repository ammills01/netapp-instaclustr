#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
: "${PGHOST:?Set the verified PostgreSQL DNS endpoint}"
: "${PGUSER:?Set the migration role}"
: "${PGDATABASE:?Set the target database, suggested instaclustr_demo_hub}"
export PGSSLMODE=verify-full
: "${PGSSLROOTCERT:?Set CA certificate path}"
psql -X -v ON_ERROR_STOP=1 -f 001_schema.sql -f 002_seed.sql
if [[ -n "${DEMO_READER_ROLE:-}" ]]; then
  psql -X -v ON_ERROR_STOP=1 -v reader_role="$DEMO_READER_ROLE" -f 003_grant_reader.sql
fi
