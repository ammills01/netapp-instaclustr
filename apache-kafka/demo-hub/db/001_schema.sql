BEGIN;
CREATE SCHEMA IF NOT EXISTS demo_hub;
REVOKE ALL ON SCHEMA demo_hub FROM PUBLIC;
CREATE TABLE IF NOT EXISTS demo_hub.integrations (
 slug text PRIMARY KEY CHECK (slug ~ '^[a-z0-9-]+$'),
 name text NOT NULL, category text NOT NULL CHECK (category IN ('commercial','opensource','analytics')),
 edition text NOT NULL, icon text NOT NULL, website_url text NOT NULL CHECK (website_url LIKE 'https://%'),
 docs_url text NOT NULL CHECK (docs_url LIKE 'https://%'), description text NOT NULL, walkthrough text NOT NULL,
 sort_order integer NOT NULL DEFAULT 100, demo_url text CHECK (demo_url LIKE 'https://%'),
 status text NOT NULL DEFAULT 'planned' CHECK (status IN ('planned','ready','maintenance')),
 published boolean NOT NULL DEFAULT true, updated_at timestamptz NOT NULL DEFAULT now(),
 CHECK (status <> 'ready' OR demo_url IS NOT NULL)
);
CREATE OR REPLACE VIEW demo_hub.public_catalog AS
 SELECT slug,name,category,edition,icon,website_url,docs_url,description,walkthrough,sort_order,
 CASE WHEN status='ready' THEN demo_url ELSE NULL END AS demo_url,status
 FROM demo_hub.integrations WHERE published;
REVOKE ALL ON ALL TABLES IN SCHEMA demo_hub FROM PUBLIC;
COMMIT;
