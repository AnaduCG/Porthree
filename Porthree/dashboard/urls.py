""" views: MainApp views
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    user_details_form,
    create_project,
    create_skill,
    create_post,
)

urlpatterns = [
    path("user-details/", user_details_form, name="user-details"),
    path("create-skills/", create_skill, name="create-skills"),
    path("create-project/", create_project, name="create-project"),
    path("edit-project/<uuid:project_id>/", create_project, name="edit-project"),
    path("create-post/", create_post, name="create-post"),
    path("edit-post/<uuid:post_id>/", create_post, name="edit-post"),

]


# the following settings are to ensured django serves files

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
