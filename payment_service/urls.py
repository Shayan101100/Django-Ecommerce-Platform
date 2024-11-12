from django.urls import path
from .views import PaymentCreateView, PaymentDetailView

urlpatterns = [
    path('payments/', PaymentCreateView.as_view(), name='Payment-create'),
    path('payments/<int:pk>', PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/orders/<int:orde>/', PaymentDetailView.as_view(), name='payment-by-order'),
    ]
