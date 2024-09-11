from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': "Ім'я користувача",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Електронна пошта',
    }))
    password1 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        'placeholder': "Пароль",
    }))
    password2 = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={
        'placeholder': "Підтвердіть пароль",
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']