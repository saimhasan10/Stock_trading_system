from django.shortcuts import render

def stock_updates(request):
    return render(request, 'live_updates/stock_updates.html')

def market_activity(request):
    return render(request, 'live_updates/market_activity.html')
