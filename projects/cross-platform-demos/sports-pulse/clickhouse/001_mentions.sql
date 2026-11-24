-- Approved ClickHouse demo cluster only; Kafka ingestion configured separately.
CREATE DATABASE IF NOT EXISTS sports_pulse;
CREATE TABLE IF NOT EXISTS sports_pulse.mentions (
 mention_id String, event_id String, sport LowCardinality(String),
 source LowCardinality(String), source_type LowCardinality(String), term String,
 published_at DateTime64(3, 'UTC'), timestamp_basis LowCardinality(String)
) ENGINE = MergeTree ORDER BY (sport, published_at, term, mention_id)
TTL toDateTime(published_at) + INTERVAL 7 DAY;
SELECT sport, term, uniqExact(event_id) AS mentions
FROM sports_pulse.mentions
WHERE published_at >= now() - INTERVAL 1 HOUR AND source_type = 'rss'
GROUP BY sport, term ORDER BY mentions DESC LIMIT 50;
