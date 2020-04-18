from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('demo/', include('demo.urls', namespace='demo')),
    path('', include('landingpage.urls', namespace='index')),
    path('auths/', include('auths.urls', namespace='auths')),
    path('feed/', include('feed.urls', namespace='feed')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('inquiry/', include('inquiry.urls', namespace='inquiry')),
    path('people/', include('people.urls', namespace='people')),
    path('noticle/', include('noticle.urls', namespace='noticle')),
    path('message/', include('message.urls', namespace='message')),
]

urlpatterns += [
    path('authmanagment/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)