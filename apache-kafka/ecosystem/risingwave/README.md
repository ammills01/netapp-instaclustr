# RisingWave
Deploy an approved edition and configure a Kafka source using https://risingwave.com/connectors/apache-kafka-source/ . Use verified TLS, scoped ACLs and supported secret management. Create a source demo_orders for topic demo.orders.v1 (order_id, region, amount, event_time). Then run:

```sql
CREATE MATERIALIZED VIEW orders_by_region AS
SELECT region, COUNT(*) AS orders, SUM(amount) AS revenue
FROM demo_orders GROUP BY region;
```
Expose only an approved authenticated SQL workspace/dashboard, never a raw database port.
