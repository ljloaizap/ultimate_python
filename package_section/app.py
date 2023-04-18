import requests

url = 'https://www.google.com.co'
r = requests.get(url=url)
print(r.status_code)
