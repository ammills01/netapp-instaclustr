# DBGorilla

Status: planned; vendor-documented Instaclustr integration, not yet deployed or tested in this lab.

- Product: https://www.dbgorilla.com/
- Pricing: https://www.dbgorilla.com/pricing (commercial, free tier available; verify engine entitlement)
- Official Instaclustr setup: https://www.dbgorilla.com/docs/connect/instaclustr/

## Demo objective
Analyze SQL workload and query performance; correlate database metrics with operational recommendations.

## Setup
Use the same isolated Sports Pulse environment. Follow the engine-specific vendor guide for the collector version, dedicated read-only role, required monitoring grants and supported versions. Use scoped read-only provisioning and monitoring API credentials where required. Keep credentials in runtime secret storage, verify TLS and restrict collector connectivity. Review which schema, workload and metrics data leaves the environment before enabling collection. Disable remote query execution and mutating actions; do not expose internal topology, sensitive SQL or private URLs through a public demo. Validate public-safe observability views and licensing before enabling Launch Live Demo. No secrets or actual deployment settings are included.
