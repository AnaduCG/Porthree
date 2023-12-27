""" views: MainApp views
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    user_logout,
    signup,
    user_login,
   
)

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    # password reset end points

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='MainApp/password_reset.html',), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='MainApp/password_reset_done.html',), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='MainApp/password_reset_confirm.html', ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='MainApp/password_reset_complete.html',), name='password_reset_complete')
]


# the following settings are to ensured django serves files

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
