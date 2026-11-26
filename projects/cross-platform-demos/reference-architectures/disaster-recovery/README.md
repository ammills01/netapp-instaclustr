# Multi-region disaster recovery

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Design and validate recovery objectives without disrupting production.

## Proposed data path
Primary region → service-specific replication → secondary region

## Technology selection
Kafka, Cassandra, PostgreSQL, Prometheus, NetApp storage where applicable. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Measure RPO and RTO in an isolated environment; validate service-specific failover.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
