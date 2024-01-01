""" views: MainApp views
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index

app_name = "MainApp"

urlpatterns = [
    path('', index, name="index"),
    ]


# the following settings are to ensured django serves files

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
