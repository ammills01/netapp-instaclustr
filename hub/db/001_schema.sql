BEGIN;
CREATE SCHEMA IF NOT EXISTS platform_hub;
REVOKE ALL ON SCHEMA platform_hub FROM PUBLIC;
CREATE TABLE IF NOT EXISTS platform_hub.catalog (
 singleton boolean PRIMARY KEY DEFAULT true CHECK(singleton),
 document jsonb NOT NULL CHECK(jsonb_typeof(document)='object'),
 updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS platform_hub.launches (
 group_slug text NOT NULL, item_slug text NOT NULL,
 status text NOT NULL DEFAULT 'planned' CHECK(status IN ('planned','ready','maintenance')),
 demo_url text CHECK(demo_url LIKE 'https://%'),
 PRIMARY KEY(group_slug,item_slug),
 CHECK(status <> 'ready' OR demo_url IS NOT NULL)
);
CREATE OR REPLACE VIEW platform_hub.public_catalog AS
SELECT c.document,
 COALESCE((SELECT jsonb_object_agg(l.group_slug || '/' || l.item_slug,
 jsonb_build_object('status',l.status,'demo_url',CASE WHEN l.status='ready' THEN l.demo_url ELSE NULL END))
 FROM platform_hub.launches l),'{}'::jsonb) AS launches
FROM platform_hub.catalog c;
REVOKE ALL ON ALL TABLES IN SCHEMA platform_hub FROM PUBLIC;
COMMIT;
