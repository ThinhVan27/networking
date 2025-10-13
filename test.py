import requests

proxies = {"http": "http://192.168.56.103:8000/hello"}

response = requests.get("http://127.0.0.1:8000/hello", proxies=proxies)
print(response.text)
