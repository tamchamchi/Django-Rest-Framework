import requests

endpoint = "http://127.0.0.1:8080/api/"

# GET Request
get_response = requests.get(endpoint)
print(get_response.json()['message'])

"""
HTTP Request -> HTML
REST API HTTP Request -> JSON
JavaScript Object Notation ~ Python Dictionary
"""