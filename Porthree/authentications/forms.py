"""
This module contains all forms for data posting
"""
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    # Add custom fields if needed
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "example@gmail.com",
                    "required": "required",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Password"}
            ),
            "password2": forms.PasswordInput(
                attrs={"class": "form-control", "placeholder": "Confirm Password"}
            ),
        }


class LoginForm(AuthenticationForm):
    pass
