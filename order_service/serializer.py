import fractions
from rest_framework import serializers
from .models import Order,OrderItem
from product_service.models import Product
import logging

logger = logging.getLogger(__name__)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Order
        fields = ['items', 'total_price','user']
    def create(self, validated_data):
        logger.debug(f"Creating order with validated data: {validated_data}")
        items_data = validated_data.pop('items', [])
        user = validated_data.pop('user')
        order = Order.objects.create(user=user,total_price=0, **validated_data)  # Initialize total_price to 0
        last_order = Order.objects.all().last()
        total_price = 0
        # Check if user is provided in validated_data
        
        for item_data in items_data:
            try:
                
                product = Product.objects.get(id=item_data['product'].id)  # Assuming product is sent as ID
                quantity = item_data['quantity']
                price = product.price * quantity

                total_price += price * quantity
                
                OrderItem.objects.create(
                    order=last_order,
                    product=product,
                    quantity=quantity,
                    price=price,
                )
            except Product.DoesNotExist:
                logger.error(f"Product with ID {item_data['product']} does not exist.")
                raise serializers.ValidationError({"product": "This product does not exist."})

        # Set the total price after processing all items
        order.total_price = total_price
        order.save()

        logger.debug(f"Total price calculated: {total_price}")
        return order

  
    def validate(self, data):
        logger.debug(f"Validating data: {data}")
        # Additional validation logic can go here
        return data
