"""
This module contains all forms for data posting to server
"""
from django.contrib.auth.models import User
from django import forms

from MainApp.models import Comment

class CommentForm(forms.ModelForm):
    """
    form to manage comments
    """
    class Meta:
        model = Comment
        fields = ['text']
