import requests

api_url = "https://randomuser.me/api/"

response = requests.get(api_url)

print(response.json())