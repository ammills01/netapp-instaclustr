# OpenSearch

Search, log analytics, ingest pipelines, and visual exploration.

Status: planned. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [OpenSearch Dashboards](integrations/dashboards/README.md) — Visualization
- [Data Prepper](integrations/data-prepper/README.md) — Data ingestion
- [Fluent Bit](integrations/fluent-bit/README.md) — Log collection
- [OpenTelemetry Collector](integrations/otel/README.md) — Telemetry

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.