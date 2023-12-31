""" views: MainApp views
"""
from django.urls import path
from .views import (
    portfolio,
    post_detail,
)

app_name = 'portfolio'

urlpatterns = [
    path("user/<username>", portfolio, name="portfolio"),
    path('posts/<slug:slug>/', post_detail, name='post-detail'),
    ]


# the following settings are to ensured django serves files

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
