from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]

class UserForm(forms.ModelForm):
    email   = forms.EmailField()

    class Meta:
        model   = User
        fields  = [
            'username',
            'email',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = [
            'photo'
        ]