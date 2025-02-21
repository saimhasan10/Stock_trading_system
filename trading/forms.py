from django import forms
from .models import Stock, TradeHistory

class BuyStockForm(forms.ModelForm):
    class Meta:
        model = TradeHistory
        fields = ['stock', 'quantity']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Stock.objects.all()
        self.fields['quantity'].widget.attrs.update({'min': '1'})

class SellStockForm(forms.ModelForm):
    class Meta:
        model = TradeHistory
        fields = ['stock', 'quantity']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pass user dynamically to filter stocks
        super().__init__(*args, **kwargs)
        if user:
            owned_stocks = TradeHistory.objects.filter(user=user, action='buy').values_list('stock', flat=True)
            self.fields['stock'].queryset = Stock.objects.filter(id__in=owned_stocks)
        self.fields['quantity'].widget.attrs.update({'min': '1'})
