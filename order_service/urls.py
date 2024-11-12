from django.urls import path
from .views import OrderDetailView, OrderListCreateView, OrderItemDetailView, OrderItemListCreateView    

urlpatterns = [
    path('orders/',OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/',OrderDetailView.as_view(), name='order-detail'),
    path('order-item/',OrderItemListCreateView.as_view(), name='orderitem-list-create'),
    path('order-item/<int:pk>/',OrderItemDetailView.as_view(), name='orderitem-detail'),
    ]
