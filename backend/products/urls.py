from django.urls import path

from .views import (ProductDetailAPIView, ProductCreateAPIView)

urlpatterns = [
    path('', ProductCreateAPIView.as_view(),),
    path('<int:pk>/', ProductDetailAPIView.as_view(),),
]