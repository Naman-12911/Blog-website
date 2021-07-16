from django.forms import ModelForm
from home.models import Login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(ModelForm):
    class Meta:
        model=Login
        fields = ['Username_or_Email', 'password']
        widgets = {
           'password':forms.PasswordInput,
        }
