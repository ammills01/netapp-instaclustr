# NetApp Instaclustr | Solution Architecture Lab

Public, independent demonstration repository for the Instaclustr ecosystem. No production or customer data, no secrets, and no claim that a catalog entry is deployed or supported by Instaclustr.

- [Demo hub](https://ammills01.github.io/netapp-instaclustr/) — GitHub Pages serves only `docs/`.
- `platforms/` — seven technology-specific integration and demo areas.
- `projects/` — shared platform API, deployment/IaC, Prometheus, Grafana and cross-platform demos.
- `hub/` — shared PostgreSQL catalog, catalog API and build utilities.
- `docs/` — publishable, static site and generated public catalog.

## Quick start
Run `python3 hub/build_catalog.py` to regenerate the bundled catalog from the manifests. Then `python3 -m http.server 8080 --directory docs`. GitHub Pages: main branch, /docs. If you change public manifests, regenerate the catalog and commit both. PostgreSQL is optional until the API is deployed; see hub/README.md.

Each integration is initially planned. Vendor capability is not a statement of managed-service support: confirm versions, networking, service restrictions, licensing and security before demo deployment. The MCP gateway is in development; keep non-public architecture, endpoints and source in an approved private repository.

## Public-repository policy
Never commit passwords, tokens, keys, certificates with private keys, license files, tfstate, customer identifiers or internal endpoints. Only sanitized sample data and approved public endpoints belong in manifests or dashboard exports. Use secrets at runtime, never inject secrets into Pages. Review public branding and third-party trademarks internally. Pin reviewed versions and test in an isolated environment. See SECURITY.md.

This clean structure supersedes the initial Kafka-only implementation. Prior commits remain in Git history.

## Public experience release
Problem-first navigation, reference architecture library, public-only ecosystem cards, verified original logo URLs where available, and an explorable Sports Pulse technical architecture. No sign-in, comparison table or guided developer-tool tours. All real live launch links remain disabled until verified against the shared Sports Pulse environment. Current sports data and trace are explicitly synthetic previews. Original logos not yet identified are text-only; source approved original files before replacing fallback. Reference architectures are proposals, not certified integrations.
