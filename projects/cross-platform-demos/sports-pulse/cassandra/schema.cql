-- Proposed. Set approved datacenter replication and create the keyspace separately.
CREATE TABLE IF NOT EXISTS sports_pulse.articles_by_sport_day (
 sport text, day date, published_at timestamp, event_id text, title text, source text,
 PRIMARY KEY ((sport, day), published_at, event_id)
) WITH CLUSTERING ORDER BY (published_at DESC, event_id ASC);
CREATE TABLE IF NOT EXISTS sports_pulse.articles_by_id (
 event_id text PRIMARY KEY, sport text, day date, published_at timestamp, title text, source text
);
-- Size time buckets and retention by actual volume; validate with approved synthetic data.
