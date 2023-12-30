from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from MainApp.models import UserDetails, Project, Skill, Post



def post_detail(request, slug):
    """
    this view manages the display of a pecific post content
    """
    post = get_object_or_404(Post, slug=slug)
    user = request.user
    try:
        # Check if data already exists for the current user
        user_details = UserDetails.objects.get(user=user)
    except (UserDetails.DoesNotExist, TypeError):
        user_details = None
    context = {
        'post': post,
        'user_details': user_details,
        'user': user
        }
    return render(request, 'portfolio/post_detail.html', context)



def portfolio(request, username):
    # this class throws error if the user's userdetails query is empty
    """
    redirection method on login or signup containing portfolio
    """
    try:
        user = get_object_or_404(User, username=username)
    except User.DoesNotExist:
        user = None
    try:
        user_details = get_object_or_404(UserDetails, user=user)
    except UserDetails.DoesNotExist:
        user_details = None
    try:
        projects = Project.objects.filter(user=user).order_by("-created_at")
    except Project.DoesNotExist:
        projects = None
    try:
        posts = Post.objects.filter(user=user).order_by("-created_at")
    except Post.DoesNotExist:
        posts = None
    try:
        value = Skill.objects.filter(user=user)
        if value:
            skills =  value[0].name.split(", ")
        else:
            skills = None
    except Skill.DoesNotExist:
        skills = None
    context = {
        "user": request.user,
        "user_details": user_details,
        "projects": projects,
        "posts": posts,
        "skills": skills,
    }
    return render(request, "portfolio/portfolio.html", context)


@login_required
def portfolio_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    user = request.user
    user_details = get_object_or_404(UserDetails, user=user)
    context = {
        "user": user,
        "user_details": user_details,
    }
    return render(request, "portfolio_nav.html", context)


def main_nav(request):
    """
    redirection method on login or signup containing portfolio
    """
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "base.html", context)
