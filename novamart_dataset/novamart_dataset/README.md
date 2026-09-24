# NovaMart Sample Dataset — Splunk Fundamentals Day 1

Synthetic, story-driven machine data for a fictional Indian e-commerce retailer, **NovaMart**.
Time window: **14-Sep-2026 00:00 to 20-Sep-2026 23:59 IST (UTC+05:30)**.
All names, customers and IP addresses are fictional. Attacker IPs use RFC 5737 documentation ranges.

## Files

| File | Host to assign | Source type | Events | Notes |
|---|---|---|---|---|
| web/web01_access.log | web01 | access_combined | 10,856 | Apache combined format |
| web/web02_access.log | web02 | access_combined | 11,785 | Apache combined format |
| app/order_service.log | app01 | novamart:app (custom) | 3,042 | ISO-8601 timestamps with +05:30, key=value + free text |
| payment/payment_gateway.json | paygw01 | novamart:payment (from _json) | 806 | One JSON object per line; timestamp field = `timestamp` |
| auth/secure.log | bastion01 | linux_secure | 1,082 | Syslog format, no year / time zone — set TZ = Asia/Kolkata |
| network/firewall.log | (sender IP) | novamart:firewall | 300 | Replayed over UDP by `send_syslog.py` (optional lab) |
| lookups/novamart_products.csv | – | lookup | 20 rows | product_id, product_name, category, unit_price, supplier |
| lookups/http_status.csv | – | lookup | 12 rows | status, status_description, status_type |
| lookups/threat_intel_ips.csv | – | lookup | 5 rows | ip, threat_category, confidence, first_seen |
| config/*.conf | – | reference | – | inputs.conf, outputs.conf, props.conf, transforms.conf |

Target index for all labs: **novamart**.

## Regenerating
The data is produced by a seeded generator, so the lab guide's expected results match this exact copy of the files.
Do not edit the files if you want the expected results to match.
