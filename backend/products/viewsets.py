from rest_framework import mixins, viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> QuerySet
    get -> retrieve -> Instance Detail view
    post -> create -> New Instance
    put -> update -> Update Instance
    patch -> partial_update -> Update Instance
    delete -> destroy -> Delete Instance
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    '''
        get -> list -> QuerySet
        get -> retrieve -> Instance Detail view
        '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


product_list = ProductGenericViewSet.as_view({'get' 'list'})
product_detail = ProductGenericViewSet.as_view({'get' 'retrieve'})
