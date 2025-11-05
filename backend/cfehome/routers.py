from rest_framework.routers import DefaultRouter
from products.viewsets import (ProductViewSet, ProductGenericViewSet)

router = DefaultRouter()

router.register(prefix='products-abc', viewset=ProductGenericViewSet, basename='products')

urlpatterns = router.urls

#print(urlpatterns)
