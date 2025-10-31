from django.http import JsonResponse

def api(request, *args, **kwargs):
    return JsonResponse({"message": "Hello From Django api app"})