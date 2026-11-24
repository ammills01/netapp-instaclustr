# Developer experience deployments
Use an isolated demo VM with access to Instaclustr Kafka. Use read-only Kafka ACLs for synthetic topics; grant writes only to a controlled producer. Verify SASL mechanism and CA trust; samples assume SASL_SSL and SCRAM-SHA-256. Never disable TLS verification. Pin reviewed versions/digests in ignored .env.

Create private/ with restrictive permissions. Copy akhq/application.example.yml to private/akhq.yml, kafbat/kafbat.env.example to private/kafbat.env, and factor-house/kpow.env.example to private/kpow.env. Populate only the selected tool's configuration; use documented license settings. Run `docker compose --profile akhq up -d` (or kafbat or kpow). These are untested scaffolds; review vendor documentation before deploying.

All ports bind to localhost. Use SSH forwarding for testing. Before publishing any URL, configure approved authenticated TLS ingress, RBAC and rate limits. Do not expose anonymous Kafka consoles or customer data. For Lenses and Conduktor see individual runbooks.
