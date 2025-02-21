from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('buy/', views.BuyStockView.as_view(), name='buy_stock'),
    path('sell/', views.SellStockView.as_view(), name='sell_stock'),
    path('trade-history/', views.TradeHistoryView.as_view(), name='trade_history'),  # Trade history page
    path('live-updates/', views.LiveUpdatesView.as_view(), name='live_updates'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('buy/', views.BuyStockView.as_view(), name='buy_stock'),
    path('sell/', views.SellStockView.as_view(), name='sell_stock'),
    path('trade-history/', views.TradeHistoryView.as_view(), name='trade_history'),  # Trade history page
    path('live-updates/', views.LiveUpdatesView.as_view(), name='live_updates'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('buy/', views.BuyStockView.as_view(), name='buy_stock'),
    path('sell/', views.SellStockView.as_view(), name='sell_stock'),
    path('trade-history/', views.TradeHistoryView.as_view(), name='trade_history'),  # Trade history page
    path('live-updates/', views.LiveUpdatesView.as_view(), name='live_updates'),
]
