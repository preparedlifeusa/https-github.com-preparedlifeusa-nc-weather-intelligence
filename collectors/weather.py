"""Fetch currently active North Carolina NWS alerts; no API key needed."""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://api.weather.gov/alerts/active?area=NC"
USER_AGENT = os.environ.get("NWS_USER_AGENT", "PreparedLifeUSA-Report4/0.1 (https://github.com/preparedlifeusa)")
OUTPUT = Path("data/nc_alerts.json")


def collect():
    request = Request(URL, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json",
    })
    with urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("type") != "FeatureCollection" or not isinstance(payload.get("features"), list):
        raise ValueError("Unexpected NWS alerts response")
    result = {
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": URL,
        "count": len(payload["features"]),
        "alerts": payload["features"],
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(f"Saved {result['count']} active NC alerts to {OUTPUT}")


if __name__ == "__main__":
    collect()
