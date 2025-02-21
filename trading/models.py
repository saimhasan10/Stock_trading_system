from django.db import models
from django.conf import settings  # Import settings to reference AUTH_USER_MODEL

class Stock(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class TradeHistory(models.Model):
    ACTION_CHOICES = [('buy', 'Buy'), ('sell', 'Sell')]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Fix here
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    price_at_time = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stock.name} ({self.action})"

    class Meta:
        ordering = ['-timestamp']
