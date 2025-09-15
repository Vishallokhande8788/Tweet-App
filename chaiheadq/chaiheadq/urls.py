from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

# Redirect root URL "/" to tweet list
def redirect_root(request):
    return redirect('tweet_list')

urlpatterns = [
    path("", redirect_root),               # Root URL redirects to tweet_list
    path("admin/", admin.site.urls),       # Admin panel
    path("tweet/", include('tweet.urls')),
    path ("accounts/", include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
