# Hybrid enterprise AI assistant

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Retrieve enterprise data and governed tools across hybrid environments.

## Proposed data path
ONTAP documents → indexing → OpenSearch / PostgreSQL pgvector → MCP → agent

## Technology selection
ONTAP, OpenSearch, PostgreSQL, pgvector, MCP Gateway. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Ask a question over approved documents with source attribution and bounded tool access.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
