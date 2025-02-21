from django.urls import path
from .views import stock_updates, market_activity

urlpatterns = [
    path('stock-updates/', stock_updates, name='stock_updates'),
    path('market-activity/', market_activity, name='market_activity'),
]
