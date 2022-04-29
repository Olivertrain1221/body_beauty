from django import forms
from .models import TattooPost
# from django.conf import settings


class CreatePost(forms.ModelForm):
    class Meta:
        model = TattooPost
        fields = ['title', 'body', 'image']

    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)


class EditPost(forms.ModelForm):
    """
    This is the Form to update the Users account
    """
    class Meta:
         model = TattooPost
         fields = ['title', 'body', 'image']