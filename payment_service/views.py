from venv import logger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from order_service.models import Order
from .serializer import PaymentSerializer
import logging

# Create your views here.
logger = logging.getLogger(__name__)

class PaymentCreateView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        
        try:
            order = Order.objects.filter(user=user).latest('ordered_at')
            amount = order.total_price
            request.data ['order']= order.id
            request.data['amount'] = str(amount)
            serializer = PaymentSerializer(data=request.data)
            if serializer.is_valid():
                payment = serializer.save(status='pending')
                
                logger.debug(f"Payment created: {payment.id}")
                payment.status = 'completed'
                payment.save()
                order.status = 'completed'
                order.save()
                return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
            else:
                logger.debug(f"Serializer error: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            logger.error(f"Order not found for user {user.id}")
            return Response({"error": "Order not found"}, status=status.HTTP_400_BAD_REQUEST)
            
            

class PaymentDetailView(APIView):
    def get(self, request, order_id=None, *arg, **kwargs):
        if order_id:
            payments = Payment.objects.filter(order__id=order_id)
            return Response(PaymentSerializer(payments, many=True).data)
        else:
            payment = self.get_object(kwargs['pk'])
            return Response(PaymentSerializer(payment).data)