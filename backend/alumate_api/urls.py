from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('health_check.urls', namespace='health_check')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/auth/', include('djoser.urls')),
    path('api/account/', include('account.urls', namespace='account')),
    path('api/post/', include('post.urls', namespace='post')),
]
