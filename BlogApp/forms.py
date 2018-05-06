from django import forms
from .models import *


class NewPostForm(forms.ModelForm):
    """Form related to Post model for creating a new Post."""
    class Meta:
        model = Post
        exclude = ['description']
