
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer
import logging

logger = logging.getLogger(__name__)
# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        try:
            order = serializer.save(user=self.request.user)
            logger.debug(f"Order created with ID: {order.id} for user: {self.request.user}")
        except Exception as e:
            logger.error(f"Error creating order: {e}")
            raise            

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=request.user)
            response_serializer = self.get_serializer(order)
            logger.debug(f"serializer response data: {response_serializer.data}")
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.debug(f"serializer error: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        order = serializer.save()
        order.calculate_total_price()
        logger.debug(f"Order with ID {order.id} updateed with new total price: {order.total.price}")
        

class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]