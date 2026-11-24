# Shared platform hub
The static UI uses docs/catalog.json generated from each platform and project manifest. A public read-only HTTPS API can replace the bundled catalog at runtime. No credentials are ever needed by GitHub Pages.

## Generate
Run python3 hub/build_catalog.py from the repository root. Commit manifests and generated docs/catalog.json together. Run python3 hub/build_catalog.py --check to detect drift.

## PostgreSQL
Suggested database: instaclustr_demo_hub; schema: platform_hub. The new schema is independent of the earlier demo_hub schema. Create the database with an authorized administrator before applying 001_schema.sql. Use PGHOST (certificate-matching DNS), PGPORT, PGDATABASE, PGUSER, PGSSLROOTCERT and an injected password/protected PGPASSFILE. Run psql -X -v ON_ERROR_STOP=1 -f hub/db/001_schema.sql with PGSSLMODE=verify-full, then run python3 hub/db/seed.py using the migration owner's DATABASE_URL and CA. Seed re-runs preserve per-tool runtime status and public demo URL; public metadata is refreshed. A migration owner can update status and demo_url in platform_hub.launches. The reader should have a separate login and no inherited write privileges; grant schema USAGE and SELECT on public_catalog via 002_grant_reader.sql. No DB has been created remotely.

## API
Install hub/api/requirements.txt. Configure the read-only role DATABASE_URL, PGSSLROOTCERT, PUBLIC_ORIGIN=https://ammills01.github.io. Run uvicorn main:app --host 127.0.0.1 --port 8000 from hub/api. Alternatively build the Dockerfile and inject environment and CA at runtime. Put an HTTPS reverse proxy with rate limiting in front; restrict database access to the backend. Set docs/config.js apiBase to the approved HTTPS API origin. Catalog is public metadata by design. CORS is not authentication. Launch URLs must require independent authentication. Never put secrets or internal endpoints in public records.
