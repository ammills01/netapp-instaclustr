-- Create a dedicated login separately through approved secret provisioning.
BEGIN;
GRANT USAGE ON SCHEMA demo_hub TO :"reader_role";
GRANT SELECT ON demo_hub.public_catalog TO :"reader_role";
COMMIT;
