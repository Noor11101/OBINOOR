from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from .models import User
# from django.forms import *
from django import forms


class signupForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'inputx', 'placeholder': 'Username'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'inputx', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'inputx', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'inputx', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#
# class ContactForm(forms.Form):
#     name =  forms.CharField(max_length=100)
#     email = forms.CharField(validators=[EmailValidator()])
#     phone = forms.CharField(max_length=15)
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#
#
#
#
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.CharField(validators=[EmailValidator()])
#     company = forms.CharField(max_length=100, required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)
