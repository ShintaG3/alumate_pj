from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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

urlpatterns +=[
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auths/password_reset_form.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auths/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='auths/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)