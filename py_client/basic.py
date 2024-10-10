import requests

endpoint = "http://127.0.0.1:8000/api/"

# GET Request
get_response = requests.get(endpoint, params={'abc':123}, json={'query': "hello world"})
print(get_response.json())

"""
HTTP Request -> HTML
REST API HTTP Request -> JSON
JavaScript Object Notation ~ Python Dictionary
"""