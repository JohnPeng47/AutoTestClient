import requests

url = "http://localhost:8000/sync"
res = requests.post(url, data={
    "last_commit": "HELLO" 
    }
)

print(res.text)