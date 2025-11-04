from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.mixins import (StaffEditorPermissionMixin, UserQuerySetMixin)

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] # authentication.TokenAuthentication

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print('serializer validated data = ', serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        # print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
        # send a Django signal here
        
    # @override
    #def get_queryset(self, *args, **kwargs):
    #    qs = super().get_queryset(*args, **kwargs)
    #    request = self.request
        # print(request.user)
        # user = request.user
        # if not user.is_authenticated:
        #     return Product.objects.none()
    #    return qs.filter(user=request.user)

class ProductDetailAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class ProductUpdateAPIView(StaffEditorPermissionMixin, UserQuerySetMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    #def perform_destroy(self, instance):
    #    super().perform_destroy(instance)


class ProductMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        #print(args, kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
