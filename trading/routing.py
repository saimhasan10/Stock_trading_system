from django.urls import re_path
from .consumers import StockUpdateConsumer

websocket_urlpatterns = [
    re_path(r'ws/stock_updates/', StockUpdateConsumer.as_asgi()),
]
