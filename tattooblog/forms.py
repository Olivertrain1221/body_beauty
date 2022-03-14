from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.TattooPost
        fields = ['title', 'body', 'slug', 'image']
