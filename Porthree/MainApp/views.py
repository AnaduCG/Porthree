from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserDetails, Project, Skill, Post


# Create your views here.
def index(request):
    """index view function

    Args:
        request (_object_): django http request

    Returns:
        _object_: interaction with template
    """
    user = request.user
    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.all().order_by("?")
    except UserDetails.DoesNotExist:
        user_details = None
    try:
        # Check if data already exists for the current user
        posts = Post.objects.all().order_by("-created_at")
    except Post.DoesNotExist:
        posts = None
    try:
        # Check if data already exists for the current user
        projects = Project.objects.all().order_by("-created_at")
    except Project.DoesNotExist:
        projects = None
    try:
        # Check if data already exists for the current user
        user_detail = UserDetails.objects.get(user=user)
    except (UserDetails.DoesNotExist, TypeError):
        user_detail = None
    context = {
        "user_details": user_details,
        "user_detail": user_detail,
        "posts": posts,
        "projects": projects,
        }
    return render(request, "MainApp/index.html", context)
