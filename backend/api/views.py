from django.http import JsonResponse
import json 

def api_home(request, *args, **kwargs):
    body = request.body
    print(request.body)
    print(request.content_type)
    data = {}
    try: 
        data = json.loads(body)
    except: 
        pass 
    print(data)
    return JsonResponse(data)
