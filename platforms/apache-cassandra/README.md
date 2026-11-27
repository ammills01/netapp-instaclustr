# Apache Cassandra

Distributed data modeling, CQL, and application integration.

Status: planned. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [cqlsh](integrations/cqlsh/README.md) — Developer tools
- [DBeaver](integrations/dbeaver/README.md) — Developer tools
- [Spark Cassandra Connector](integrations/spark-connector/README.md) — Analytics
- [Cassandra Reaper](integrations/reaper/README.md) — Operations reference
- [Cassandra Medusa](integrations/medusa/README.md) — Operations reference

- [DBGorilla](integrations/dbgorilla/README.md) — Database observability

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.