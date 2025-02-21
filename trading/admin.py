from django.contrib import admin
from .models import Stock, TradeHistory

# Customizing the display of the Stock model in the admin panel
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'price')  # Columns to show in the list view
    search_fields = ('name', 'symbol')  # Enable searching by name and symbol
    list_filter = ('name',)  # Enable filtering by stock name

# Customizing the display of the TradeHistory model in the admin panel
class TradeHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'stock', 'quantity', 'action', 'price_at_time', 'timestamp')  # Columns to show
    search_fields = ('user__username', 'stock__name', 'action')  # Enable searching by user, stock name, and action
    list_filter = ('action', 'timestamp')  # Enable filtering by action and timestamp
    ordering = ('-timestamp',)  # Order by timestamp (most recent first)

# Register the models with their custom admin configuration
admin.site.register(Stock, StockAdmin)
admin.site.register(TradeHistory, TradeHistoryAdmin)
