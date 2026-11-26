# Edge-to-cloud industrial IoT

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Stream sensor telemetry, retain edge data, and trigger maintenance.

## Proposed data path
Edge ONTAP → Kafka → Cassandra / ClickHouse → Spark → Cadence

## Technology selection
NetApp ONTAP, Kafka, Cassandra, ClickHouse, Spark, Cadence, Grafana. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Compare recent readings, aggregate trends and maintenance triggers.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
