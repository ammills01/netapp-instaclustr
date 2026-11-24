# ClickHouse

High-throughput analytical SQL, BI, and Kafka ingestion.

Status: planned. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [Grafana](integrations/grafana/README.md) — Visualization
- [Apache Superset](integrations/superset/README.md) — Business intelligence
- [dbt](integrations/dbt/README.md) — Data transformation
- [Kafka ingestion](integrations/kafka-ingestion/README.md) — Streaming integration
- [DBeaver](integrations/dbeaver/README.md) — SQL client

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.