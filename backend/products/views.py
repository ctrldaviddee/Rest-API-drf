from django.template.defaultfilters import title
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print('serializer validated data = ', serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a Django signal here

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save(title=title)

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    #def perform_destroy(self, instance):
    #    super().perform_destroy(instance)

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    if request.method == 'GET':

        if pk is not None:
            # detail view
            return Response(
                ProductSerializer(
                    get_object_or_404(Product, pk=pk),
                    many=False
                ).data
            )

        # list view
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data['title']
            content = serializer.validated_data['content'] or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return None