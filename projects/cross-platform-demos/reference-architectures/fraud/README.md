# Real-time fraud detection

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Detect suspicious transactions without blocking operational ingestion.

## Proposed data path
Kafka → streaming rules → ClickHouse / Cassandra → Cadence

## Technology selection
Kafka, ClickHouse, Cassandra, Cadence. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Detect a synthetic anomaly and open a case workflow.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
