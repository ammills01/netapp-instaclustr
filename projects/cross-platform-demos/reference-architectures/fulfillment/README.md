# Order fulfillment

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Coordinate payments, inventory and shipping despite failures.

## Proposed data path
PostgreSQL → Cadence → Kafka → Cassandra

## Technology selection
PostgreSQL, Cadence, Kafka, Cassandra. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Inspect retries and compensation in a synthetic order workflow.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
