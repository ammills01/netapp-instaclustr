# Apache Kafka

Event streaming, developer experience, and real-time processing.

Status: planned. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [Factor House · Kpow](integrations/kpow/README.md) — Commercial DevEx
- [Lenses.io](integrations/lenses/README.md) — Commercial DevEx
- [Conduktor](integrations/conduktor/README.md) — Commercial DevEx
- [AKHQ](integrations/akhq/README.md) — Open-source DevEx
- [Kafbat UI](integrations/kafbat/README.md) — Open-source DevEx
- [RisingWave](integrations/risingwave/README.md) — Stream processing
- [Streambased](integrations/streambased/README.md) — Iceberg analytics
- [Kafka Connect](integrations/kafka-connect/README.md) — Data integration

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.