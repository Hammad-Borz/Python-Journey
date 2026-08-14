import requests
response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    params={"id": 3}
)
print(response.status_code)
data = response.json()
print(data)
print(data[0]["name"])
for user in data:
    print("Name:", user["name"])
    print("Email:", user["email"])