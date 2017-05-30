from django.conf.urls import include, url

from main_app.views import home
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = [
    url(r'login/', include('shopify_auth.urls')),
    url(r'app/', include('main_app.urls')),
    url(r'^$', home, name='home')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
