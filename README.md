# Report 4 — North Carolina Weather Intelligence

Free-first prototype for collecting public National Weather Service alerts for North Carolina.

## Run locally

Python 3.11+ required.

```bash
python collectors/weather.py
```

Output: `data/nc_alerts.json` (generated; not committed).

## Automation

GitHub Actions runs the collector every hour and supports manual runs. Outputs are retained as workflow artifacts for seven days. GitHub Actions schedules may be delayed.

## Authentication

The public NWS alerts API does not require a credential. This prototype does not store AWS keys, GitHub tokens, or other secrets. GitHub Actions has read-only repository permission; no AWS access is configured.

## Next phases

- Build and verify an authoritative 100-county NC registry with FIPS and geometry identifiers.
- Add county-by-county alert aggregation and weather observations.
- Add validation, monitoring, tests, and durable storage.
- If AWS is introduced, use GitHub OIDC with narrowly scoped IAM roles instead of long-lived access keys.

## Data source

National Weather Service API: https://www.weather.gov/documentation/services-web-api
