from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('health_check.urls', namespace='health_check')),
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls', namespace='account')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
