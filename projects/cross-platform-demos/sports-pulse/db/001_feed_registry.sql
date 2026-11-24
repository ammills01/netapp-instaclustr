BEGIN;
CREATE SCHEMA IF NOT EXISTS sports_pulse;
REVOKE ALL ON SCHEMA sports_pulse FROM PUBLIC;
CREATE TABLE IF NOT EXISTS sports_pulse.feeds (
 id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY, sport text NOT NULL,
 source_name text NOT NULL, feed_url text NOT NULL UNIQUE, enabled boolean NOT NULL DEFAULT false,
 etag text, last_modified text, last_poll_at timestamptz, last_success_at timestamptz
);
COMMIT;
