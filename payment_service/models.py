from django.db import models

class Payment(models.Model):
    order = models.ForeignKey('order_service.Order', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment {self.id} - Orde {self.order.id} - Status: {self.status} - Amount: {self.amount}"
# Create your models here.
