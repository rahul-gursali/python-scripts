import requests

url = "https://example.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is UP")
    else:
        print(f"{url} returned {response.status_code}")
except requests.exceptions.RequestException:
    print(f"{url} is DOWN")
