import random
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SHIPPED','Shipped'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return f"Order #{self.id} - {self.user.username} - {self.status}"

    def calculate_total_price(self):
        self.total_price = sum(item.price * item.quantity for item in self.items.all())
        self.save()
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product_service.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        #if self.order is None:
         return f"{self.product.name} X {self.quantity} for Order #{self.order.objects.all().last()}"
        #return f"{self.product.name} X {self.quantity} (Order not set)"
    
        #super().save(*arg, **kwargs)
        
    