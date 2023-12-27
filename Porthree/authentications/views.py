from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect(
                "login",
            )  # redirect to user portfolio view
    else:
        form = SignUpForm()
    return render(request, "authentications/sign-up.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("user-details")  # redirect to user portfolio view
    else:
        form = LoginForm()
    return render(request, "authentications/login.html", {"form": form})


def user_logout(request):
    """logs out a logged in user

    Args:
        request (_object_): django http request

    Returns:
        _object_: page redirection
    """
    logout(request)
    return redirect("login")  # Change 'home' to desired redirect URL
