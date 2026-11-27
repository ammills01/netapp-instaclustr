# DataGrip (JetBrains)
Status: planned; desktop client, not a browser-hosted Kafka console.
- Official product: https://www.jetbrains.com/datagrip/
- JDBC documentation: https://www.jetbrains.com/help/datagrip/jdbc-drivers.html
- Licensing: commercial subscription for commercial use; free non-commercial individual license subject to JetBrains terms: https://www.jetbrains.com/non-commercial/
- Official brand assets: https://www.jetbrains.com/company/brand/

## Kafka integration
DataGrip does not itself provide native Kafka SQL support. Use the third-party, experimental [KafCacheQL JDBC driver](../kafcacheql/README.md). Upstream setup: https://github.com/ifnesi/kafcacheql/blob/main/docs/tools.md (upstream tested DataGrip 2026.3). Use Java 21+, Generic SQL, and a reviewed driver build. Configure a scoped read-only Sports Pulse Kafka principal and verified TLS, using a private settings file. Never distribute credentials through the public hub. Test against approved demo data before enabling any live launch. Commercial demo licensing and desktop access model require review.