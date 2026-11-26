# Databricks & Snowflake integration

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Connect operational streams to existing enterprise analytics investments.

## Proposed data path
PostgreSQL → Kafka → ClickHouse + Databricks or Snowflake

## Technology selection
PostgreSQL, Kafka, ClickHouse, Databricks, Snowflake. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Compare low-latency operational aggregates with enterprise analytical workloads.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
