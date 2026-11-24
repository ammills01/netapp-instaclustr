-- Run psql -v reader_role=platform_hub_reader -f 002_grant_reader.sql
-- Create the dedicated login separately through approved credential provisioning.
BEGIN;
GRANT USAGE ON SCHEMA platform_hub TO :"reader_role";
GRANT SELECT ON platform_hub.public_catalog TO :"reader_role";
COMMIT;
