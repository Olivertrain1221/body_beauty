from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileFormUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []
