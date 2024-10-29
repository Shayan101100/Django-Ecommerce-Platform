from django.urls import path
from .views import (
    ProductDetailView, ProductListCreateView,
    CartListCreateView, CartDetailView,
    OrderListCreateView, OrderDetailView,
    OrderItemListCreateView, OrderItemDetailView
)
urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/',CartDetailView.as_view(), name='cart-detail'),
    path('orders/',OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:pk>/',OrderDetailView.as_view(), name='order-detail'),
    path('order-item/',OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-item/<int:pk>/',OrderItemDetailView.as_view(), name='orderitem-detail'),
    ]
