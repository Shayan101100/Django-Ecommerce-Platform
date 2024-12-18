from django.urls import path
from .views import (
    ProductDetailView, ProductListCreateView,
    CartListCreateView, CartDetailView
)
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/',CartDetailView.as_view(), name='cart-detail'),
    
    ]
