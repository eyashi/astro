import requests

endpoint = "http://api.burningsoul.in/moon/"
headers = {'Content-Type': 'application/json'}

resp = requests.get(endpoint)

print(resp.text)
