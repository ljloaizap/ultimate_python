import requests

r = requests.get(url='https://www.google.com.co', timeout=30)
print(r.status_code)
