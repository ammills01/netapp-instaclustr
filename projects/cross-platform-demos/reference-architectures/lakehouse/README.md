# Open lakehouse

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Retain stream data in open table formats with independent compute.

## Proposed data path
Kafka → supported Iceberg writer/catalog → StorageGRID → Spark / Trino

## Technology selection
Kafka, Apache Iceberg, NetApp StorageGRID, Spark, Trino. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Query the same approved Iceberg tables with multiple engines.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
