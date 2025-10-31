from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product

@api_view(['GET', 'POST'])
def api(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(instance=model_data, fields=['id', 'title', 'price',])
    return Response(data)