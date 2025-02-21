
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('core.urls')),
    path('trading/', include('trading.urls')),
    path('live_updates/', include('live_updates.urls')),
]
