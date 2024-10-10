from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    """
    request -> HttpRequest -> Django
    request.body
    """
    body = request.body # byte string of JSON data
    data = {}
    print(request.GET)
    print(request.POST)
    try:
        data = json.loads(body) # string of JSON data -> dictionary Python
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)