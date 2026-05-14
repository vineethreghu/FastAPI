import requests

url = "http://localhost:8000/system"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())