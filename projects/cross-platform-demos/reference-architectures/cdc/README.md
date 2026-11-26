# Change data capture

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Keep downstream search and analytics in sync with transactional changes.

## Proposed data path
PostgreSQL → Debezium / Kafka Connect → Kafka → ClickHouse + OpenSearch

## Technology selection
PostgreSQL, Debezium, Kafka, ClickHouse, OpenSearch. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Change a synthetic order and compare downstream state and lag.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
