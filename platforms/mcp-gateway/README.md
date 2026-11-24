# MCP Gateway

An evolving gateway project for governed access to tools and data. Public information only.

Status: in-development. All tools below are candidates; no live deployments are claimed.

## Integration catalog
- [MCP Inspector](integrations/inspector/README.md) — Developer tools
- [MCP TypeScript SDK](integrations/typescript-sdk/README.md) — SDK
- [MCP Python SDK](integrations/python-sdk/README.md) — SDK
- [MCP specification](integrations/protocol/README.md) — Reference

## Layout
- integrations/: product-specific configuration and runbooks
- demos/: customer walkthroughs and synthetic data
- deployment/: reviewed infrastructure and environment-specific templates
- manifest.json: public metadata consumed by the shared hub

Use the shared projects for monitoring and provisioning rather than duplicating secrets or infrastructure. Confirm managed-service compatibility before configuring each tool.