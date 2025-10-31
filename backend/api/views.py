import json
from django.http import JsonResponse

def api(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(s=body)
    except:
        pass
    data['params'] = dict(request.GET);
    data['headers'] = dict(request.headers);
    data['content_type'] = request.content_type;
    return JsonResponse(data)