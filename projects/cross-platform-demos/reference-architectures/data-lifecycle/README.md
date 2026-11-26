# Hot-to-cold data lifecycle

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Serve recent data at low latency while retaining historical records efficiently.

## Proposed data path
Kafka → ClickHouse hot data → Iceberg / object storage historical data

## Technology selection
Kafka, ClickHouse, Iceberg, StorageGRID. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Compare hot and historical queries and retention trade-offs.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
