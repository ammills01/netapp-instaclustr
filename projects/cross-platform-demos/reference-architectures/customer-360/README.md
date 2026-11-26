# Real-time customer 360

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Combine operational and behavioral data for a current customer view.

## Proposed data path
PostgreSQL / applications → Kafka → Cassandra / ClickHouse

## Technology selection
Kafka, PostgreSQL, Cassandra, ClickHouse. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Explore a synthetic customer profile and historical engagement.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
