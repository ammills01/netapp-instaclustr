# Real-time sports intelligence

**Status:** Sample preview. Proposed design, not certified or deployed.

## Customer problem
Turn continuously arriving sports news into searchable, analytical and AI-accessible intelligence.

## Proposed data path
X / RSS → Kafka → processing → ClickHouse / Cassandra / OpenSearch / PostgreSQL → Sports Pulse + MCP

## Technology selection
Kafka, ClickHouse, Cassandra, OpenSearch, PostgreSQL, Cadence, MCP, Grafana. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Explore a sample headline and trace the planned data path. Live services are not connected.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
