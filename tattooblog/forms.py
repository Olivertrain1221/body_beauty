from django import forms
from . import models


class CreatePost(forms.ModelForm):
    class Meta:
        model = models.TattooPost
        fields = ['title', 'body', 'image']

    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
