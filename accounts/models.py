from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10000.00)  
    phone_number = models.CharField(max_length=15, blank=True, null=True)  
    is_premium = models.BooleanField(default=False)  
    date_of_birth = models.DateField(blank=True, null=True)  
