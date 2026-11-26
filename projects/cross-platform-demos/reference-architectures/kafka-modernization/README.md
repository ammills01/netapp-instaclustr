# Modernize Kafka

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Migrate from an existing Kafka distribution while retaining client compatibility and independent tooling.

## Proposed data path
Existing Kafka → MirrorMaker 2 → Instaclustr Kafka → developer tools

## Technology selection
Kafka, MirrorMaker 2, AKHQ, Conduktor, Kpow, Kafbat, Lenses. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Replicate a topic and verify offsets, record counts and cutover readiness.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
