import requests
import csv
import json

CSV_URL = "https://www.vpngate.net/api/iphone/"
CSV_FILE = "vpngate.csv"
JSON_FILE = "vpngate.json"

def fetch_and_convert():
    res = requests.get(CSV_URL, timeout=30)
    res.raise_for_status()

    # Remove comments (#, *)
    raw = "\n".join([
        line for line in res.text.splitlines()
        if not line.startswith("#") and line.strip()
    ])

    # Save cleaned CSV
    with open(CSV_FILE, "w", encoding="utf-8") as f:
        f.write(raw)

    # Convert CSV → JSON
    reader = csv.DictReader(raw.splitlines())
    data = list(reader)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    fetch_and_convert()
    print("✅ Updated vpngate.csv and vpngate.json")
