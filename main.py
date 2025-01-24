import requests
from urllib.request import urlretrieve
url = 'https://21f6-84-54-83-43.ngrok-free.app/api/advertisements'

response = requests.get(url)
print(response.status_code)
print(response.json())
print(response.json()[0]['video'])

urlretrieve(f"{response.json()[0]['video']}", f"{response.json()[0]['title']}")