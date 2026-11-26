# Cloud-native storage and analytics

**Status:** Proposed. Proposed design, not certified or deployed.

## Customer problem
Pair managed data services with cloud-native NetApp storage where supported.

## Proposed data path
Managed PostgreSQL / ClickHouse → approved NetApp cloud storage integration

## Technology selection
FSx for NetApp ONTAP, Azure NetApp Files, Google Cloud NetApp Volumes, PostgreSQL, ClickHouse. Confirm versions, licensing, networking, service boundaries, and managed-service compatibility; third-party and NetApp storage combinations are candidates until verified.

## Demonstration objective
Evaluate documented service/storage combinations, not assumed cross-cloud parity.

## Implementation checklist
- Document ingestion volume, velocity and access requirements.
- Validate individual integrations and security boundaries in an isolated environment.
- Record schemas, data paths, operational trade-offs, cost and recovery considerations.
- Publish only approved public-safe data and read-only demo links.
