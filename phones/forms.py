from django import forms

from phones.models import Order


class CreateOrder(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Ваше ім'я",
    }))
    surname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ваше прізвище',
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Номер телефону',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Ваша електронна пошта',
    }))

    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number', 'email']
