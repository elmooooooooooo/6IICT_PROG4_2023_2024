import requests

respone_json = requests.get(url="http://172.16.1.107:5000/").json()

print(respone_json)