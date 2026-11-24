# Cadence

Durable execution, workflow debugging, and resilient applications.

Status: planned. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [Cadence Web](integrations/cadence-web/README.md) — Developer tools
- [Cadence CLI](integrations/cadence-cli/README.md) — Developer tools
- [Go SDK](integrations/go-sdk/README.md) — Application integration
- [Java SDK](integrations/java-sdk/README.md) — Application integration

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.