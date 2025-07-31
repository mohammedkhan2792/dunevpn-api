import requests

url = "https://www.vpngate.net/api/iphone/"

response = requests.get(url)
if response.status_code != 200:
    raise Exception("Failed to fetch VPNGate data")

raw = response.text
parts = raw.split("#")
if len(parts) < 2:
    raise Exception("Invalid data format")

csv_data = parts[1].replace("*", "").strip()

with open("vpngate.csv", "w", encoding="utf-8") as f:
    f.write(csv_data)

print("VPN CSV updated successfully.")