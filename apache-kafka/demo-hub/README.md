# Kafka Ecosystem Demo Hub
NetApp-inspired solution architect demonstration project. Custom letter icons, not official third-party logos. Review brand use internally before public publication.

## Frontend
Copy these directories into the repository root without deleting existing files. From the root run `python -m http.server 8080 --directory docs` and open http://localhost:8080. Set repository Settings > Pages > Deploy from a branch > main > /docs > Save. Expected Pages URL: https://ammills01.github.io/netapp-instaclustr/ (not live until configured). No database is needed for the bundled seven-tool catalog, filters, documentation and walkthroughs.

## PostgreSQL
Suggested database: `instaclustr_demo_hub`; schema: `demo_hub`; table: `integrations`; view: `public_catalog`.
Provision the dedicated database via Instaclustr or an authorized owner. If permitted, `createdb instaclustr_demo_hub` with PGHOST, PGUSER, PGSSLROOTCERT and PGSSLMODE=verify-full set. Otherwise ask the platform admin. Use a DNS name matching the certificate (an IP only if the certificate covers it). Set PGDATABASE, PGHOST, PGPORT, PGUSER, PGSSLROOTCERT and protected PGPASSFILE or injected password. Run `bash apache-kafka/demo-hub/db/bootstrap.sh`. This creates schema/table/view and inserts seven records. Rerunning updates metadata, preserving demo URLs/status/published flags.

Create a distinct login `demo_hub_reader` via approved secret provisioning, no elevated roles or inherited write permissions. Grant CONNECT if necessary. Set DEMO_READER_ROLE=demo_hub_reader before running bootstrap or use `psql -X -v ON_ERROR_STOP=1 -v reader_role=demo_hub_reader -f 003_grant_reader.sql` inside db/. Reader receives only USAGE on schema and SELECT on public view. Audit inherited roles and PUBLIC grants.

## API deployment
Use a host with private network access to Postgres. Copy api/.env.example to api/.env and set DATABASE_URL (URL-encode credentials), PUBLIC_ORIGIN and CA file path. Supply the CA certificate in api/private/postgres-ca.pem readable by the container's non-root user. Run `docker compose up -d --build` in api/. Front it with HTTPS ingress and rate limiting. Port binds to loopback. CORS is not authentication; catalog API is intentionally public, read-only metadata. Keep customer identifiers, private hosts, tokens, keys and license details out of the public catalog. Restrict DB access to the API/migration hosts.

Check `/healthz` and `/api/catalog` via HTTPS. Set `apiBase` in docs/config.js to your public HTTPS API origin (no secrets), commit and republish. The bundled catalog remains available when API is unreachable. The API does not probe tool health.

## Register a demo
Once authentication and access are validated, set the row's public approved URL and status as migration owner:

```sql
UPDATE demo_hub.integrations
SET demo_url='https://approved-demo.example.com', status='ready', updated_at=now()
WHERE slug='akhq';
```
This is an illustrative URL only. Set status=maintenance to disable the launch button. Set published=false to hide a row from the API (bundled snapshot remains static). Refresh the bundled metadata as needed, never include private URLs. Ready means operator-approved, not health-checked.

## Tools and security
See ../devx/README.md and ../ecosystem/ for deployment templates/runbooks. Use an isolated Kafka cluster, synthetic data, separate read-only credentials, SSO or approved equivalent, and reviewed image versions. Do not commit credentials, tokens, license keys, real .env files or customer data. GitHub secrets can be used only for controlled deployments, never injected into static HTML or JS. Use a runtime secret manager. Enable secret scanning/push protection as available; rotate exposed credentials immediately. No infrastructure has been deployed or tested against Instaclustr yet.
