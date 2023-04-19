import requests

# # GET
# url = 'https://jsonplaceholder.typicode.com/users'
# response = requests.get(url, timeout=10)
# response = response.json()
# for user in response:
#     print(user['name'])

# # GET/<id>
# url = 'https://jsonplaceholder.typicode.com/users/7'
# response = requests.get(url, timeout=10)
# print(response.json())

# # POST
# url = 'https://jsonplaceholder.typicode.com/users'
# user = {
#     'name': 'Mi chanchito'
# }
# response = requests.post(url, data=user, timeout=10)
# print(response.status_code)

# # PUT
# url = 'https://jsonplaceholder.typicode.com/users/2'
# user = {
#     'name': 'Mi chanchito'
# }
# response = requests.put(url, data=user, timeout=10)
# print(response.status_code)

# DELETE
url = 'https://jsonplaceholder.typicode.com/users/2'
apikey = 'apikey'
headers = {
    'Authorization': f'Bearer {apikey}'
}
response = requests.put(url, timeout=10, headers=headers)
print(response.status_code)
