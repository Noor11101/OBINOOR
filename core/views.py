from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from .models import User
from django.shortcuts import render, redirect
from .forms import signupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
# from django.core.mail import EmailMessage ,send_mail
from django import forms


def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Product(request):
    return render(request, 'products.html')



def Terms(request):
    return render(request, 'Terms-and-Condition.html')

def Privacy_Policy(request):
    return render(request, 'Privacy-Policy.html')

class SignupView(CreateView):
    model = User
    form_class = signupForm
    template_name = 'sign_up.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return super(SignupView, self).get(*args, **kwargs)

def Login_page(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        elif request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                print("Invalid username or password")
                return redirect('login')

def Logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Profile(request):
    return render(request, 'profile.html')

# @method_decorator(login_required(login_url='login') , name='dispatch')
# class AccountSettingsView(UpdateView):
#     model = User
#     fields = ['first_name', 'last_name', 'profile_pic' , 'bio']
#     template_name = 'account_settings.html'
#     success_url = '/profile/'

#     def get_object(self, queryset=None):
#         return self.request.user
    
    
    
def Contact_view(request):
    return render(request, 'contact.html')



@method_decorator(login_required(login_url='login'), name='dispatch')
class AccountSettingsView(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'profile_pic', 'bio']
    template_name = 'account_settings.html'
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user

    # Override the get_form method to add custom widgets
    def get_form(self, form_class=None):
        form = super(AccountSettingsView, self).get_form(form_class)
        form.fields['first_name'].widget = forms.TextInput(attrs={
            'class': 'inputx',  # Add your CSS class here
            'placeholder': 'First Name'
        })
        form.fields['last_name'].widget = forms.TextInput(attrs={
            'class': 'inputx',
            'placeholder': 'Last Name'
        })
        form.fields['profile_pic'].widget = forms.FileInput(attrs={
            'class': 'upload'
        })
        form.fields['bio'].widget = forms.Textarea(attrs={
            'class': 'inputx',
            'placeholder': 'bio , Tell us about yourself',
            'autocomplete': 'off'
        })
        return form


# def Contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             EmailMessage(
#                 'Contact Form Submission from {}'.format(name),
#                 message,
#                 '',  # Send from (your website)
#                 [''],  # Send to (your admin email)
#                 [],
#                 reply_to=[email]  # Email from the form to get back to
#             ).send()
#
#             return redirect('success')
#     else:
#         form = ContactForm()
#
#     return render(request, 'contact.html', {'form': form})
#
#
# def Success(request):
#     return HttpResponse('Success!')
#
#
