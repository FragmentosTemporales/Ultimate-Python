import requests
#url = "https://jsonplaceholder.typicode.com/users"

#r = requests.get(url, timeout=10)
# print(
#     r.status_code,
#     r.text
#     )

#r = r.json()

#for user in r:
#    print(user["name"])
    
#url2 = "https://jsonplaceholder.typicode.com/users/1"
#res = requests.get(url2, timeout=10)
#print(res.json())

url = "https://jsonplaceholder.typicode.com/users/1"
user = {
    "name": "Cristian"
}
r = requests.put(url, timeout=10)
print(r.status_code)
