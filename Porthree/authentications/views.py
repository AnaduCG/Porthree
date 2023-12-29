from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm

def logout_required(view_func):
    """
    decorator function to ensure signup view 
    is available only when user is not logged in
    """
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is logged in, redirect to the dashboard url
            DASHBOARD_URL = "user-details"
            return redirect(DASHBOARD_URL)
        return view_func(request, *args, **kwargs)

    return _wrapped_view

@logout_required
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

@logout_required
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
