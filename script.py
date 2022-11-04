import requests


r = requests.get("https://yahoo.com")
print(r.status_code)
