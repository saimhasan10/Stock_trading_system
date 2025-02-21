from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BuyStockForm, SellStockForm
from .models import Stock, TradeHistory

# Update the dashboard to show the balance
from django.db.models import Sum

class DashboardView(TemplateView):
    template_name = 'trading/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = Stock.objects.all()  # Get all available stocks
        
        # Calculate the user's balance
        total_spent = TradeHistory.objects.filter(user=self.request.user, action='buy').aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_received = TradeHistory.objects.filter(user=self.request.user, action='sell').aggregate(Sum('quantity'))['quantity__sum'] or 0

        # Assuming price_at_time reflects the purchase/sale price, so balance calculation can be like this:
        balance = total_received - total_spent
        context['balance'] = balance

        return context

# In BuyStockView - After form validation
class BuyStockView(TemplateView):
    template_name = 'trading/buy_stock.html'

    def get(self, request, *args, **kwargs):
        form = BuyStockForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = BuyStockForm(request.POST)
        if form.is_valid():
            stock = form.cleaned_data['stock']
            quantity = form.cleaned_data['quantity']
            price_at_time = stock.price  # Use stock price for buy transaction

            # Create TradeHistory entry
            TradeHistory.objects.create(
                user=request.user,
                stock=stock,
                quantity=quantity,
                action='buy',
                price_at_time=price_at_time
            )
            return redirect('trade_history')  # Redirect to history page

        return render(request, self.template_name, {'form': form})

# In SellStockView - After form validation
class SellStockView(TemplateView):
    template_name = 'trading/sell_stock.html'

    def get(self, request, *args, **kwargs):
        form = SellStockForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SellStockForm(request.POST)
        if form.is_valid():
            stock = form.cleaned_data['stock']
            quantity = form.cleaned_data['quantity']
            price_at_time = stock.price  # Use stock price for sell transaction

            # Create TradeHistory entry
            TradeHistory.objects.create(
                user=request.user,
                stock=stock,
                quantity=quantity,
                action='sell',
                price_at_time=price_at_time
            )
            return redirect('trade_history')  # Redirect to history page

        return render(request, self.template_name, {'form': form})


class TradeHistoryView(TemplateView):
    template_name = 'trading/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trade_history'] = TradeHistory.objects.filter(user=self.request.user)  # Show user's trade history
        return context

class LiveUpdatesView(TemplateView):
    template_name = "trading/live_updates.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = Stock.objects.all()  # Get all available stocks for live updates
        return context
