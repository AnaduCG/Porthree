"""
This module contains all forms for data posting to server
"""
from django.contrib.auth.models import User
from django import forms

from MainApp.models import UserDetails, Skill, Project, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "post_image", "content"]

        widgets = {
                "title": forms.TextInput(
                    attrs={"class": "form-control", "placeholder": "Project title here"}
                ),
                "content": forms.Textarea(
                    attrs={"class": "form-control", "placeholder": "Write about project..."}
                ),
            }
