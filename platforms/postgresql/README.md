# PostgreSQL

SQL development, query performance and change data capture.

Status: planned. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [pgAdmin](integrations/pgadmin/README.md) — Developer tools
- [DBeaver](integrations/dbeaver/README.md) — Developer tools
- [Debezium](integrations/debezium/README.md) — Change data capture
- [pgbench](integrations/pgbench/README.md) — Performance
- [PgBouncer](integrations/pgbouncer/README.md) — Connection pooling

- [DBGorilla](integrations/dbgorilla/README.md) — Database observability

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.