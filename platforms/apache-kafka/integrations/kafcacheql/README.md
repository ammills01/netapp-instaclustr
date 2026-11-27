# KafCacheQL
- Upstream: https://github.com/ifnesi/kafcacheql
- License: Apache 2.0
- Status: experimental; not recommended for production by upstream. Planned integration, no live endpoint.
- Requirements: Java 21+, Kafka 3.1+, compatible JDBC client (DataGrip or DBeaver).

The JDBC driver exposes Kafka topics as SQL tables, fetches records into a local SQLite cache, and executes SELECT queries over a consistent cached snapshot. It supports filters, joins and aggregations, incremental cache refresh and offline queries. It is not a real-time streaming SQL engine.

## Sports Pulse validation
Use the same Sports Pulse Kafka cluster as the other developer experience tools. Start with a bounded append-topic window, a dedicated read-only principal, verified TLS and approved redistributable data. Verify SCRAM with the selected version (upstream documents SASL/PLAIN as tested; do not assume SCRAM support is validated). The cache is unencrypted and survives Kafka access revocation. Protect and delete it as appropriate; listing filters are not ACLs. Do not expose or share the cache publicly.

Driver class: `io.github.ifnesi.kafcacheql.driver.KafCacheQLDriver`.
Example URL: `jdbc:kafcacheql://BROKER_DNS:PORT?config.file=~/private/client.properties`.
Keep authentication exclusively in private configuration. Pin and review driver code/artifacts before use.

Illustrative read-only SQL (requires live data and verified field inference):
```sql
SELECT sport, count(*) AS articles
FROM "sports.news.raw.v1"
GROUP BY sport;
```

Upstream: [client setup](https://github.com/ifnesi/kafcacheql/blob/main/docs/tools.md), [configuration](https://github.com/ifnesi/kafcacheql/blob/main/docs/configuration.md).
