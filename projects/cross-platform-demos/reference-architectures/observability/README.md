# Unified observability

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Correlate infrastructure metrics, logs and application events.

## Proposed data path
OpenTelemetry / Fluent Bit → Kafka → OpenSearch / ClickHouse → Grafana

## Technology selection
Kafka, OpenSearch, ClickHouse, Prometheus, Grafana. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Explore correlated logs and metrics from a synthetic incident.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
