from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    This is the Form to create the Users account
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AccountUpdateForm(forms.ModelForm):
    """
    This is the Form to update the Users account
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileFormUpdate(forms.ModelForm):
    """
    This is the Form to update the Users profile
    """
    class Meta:
        model = Profile
        fields = ['profile_image']


class DeleteUserForm(forms.ModelForm):
    """
    This is the Delete to create the Users account
    """
    class Meta:
        model = User
        fields = []
