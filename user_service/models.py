from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class UserInfo(AbstractUser):
    fullname = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.TextField(blank=False)
    city = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=20, blank=False)
    postal_code = models.CharField(max_length=10, 
                                   validators=[RegexValidator(regex=r'^\d{5}(-\d{4})?$', 
                                                              message='Enter a valid postal code (e.g., 12345 or 12345-6789).')],
                                   blank=False, )
    policy_agreement = models.BooleanField(default=False, blank=False)
    policy_agreement_timestamp = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.email
    def save(self, *args, **kwargs):
        if self.email:
            self.username = self.email
        super().save(*args, **kwargs)