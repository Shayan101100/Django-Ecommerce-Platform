
from rest_framework import generics
from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes =[IsAuthenticated]

class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) #assign authenticated user to 'user' field
        
class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]