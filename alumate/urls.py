from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls', namespace='demo')),
    path('', include('landingpage.urls', namespace='index')),
    path('auths/', include('auths.urls', namespace='auths')),
    path('feed/', include('feed.urls', namespace='feed')),
    path('account/', include('account.urls', namespace='account')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('inquiry/', include('inquiry.urls', namespace='inquiry')),
    path('people/', include('people.urls', namespace='people')),
]
