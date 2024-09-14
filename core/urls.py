from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('about/', About, name='about'),
    path('products/', Product, name='product'),
    path('contact/', Contact_view, name='contact'),
    path('terms-and-Condition/', Terms , name='terms'),
    path('privacy-policy/',  Privacy_Policy , name='privacy-policy'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', Login_page, name='login'),
    path('logout/', Logout_user, name='logout'),
    path('profile/', Profile, name='profile'),
    path('account-settings/', AccountSettingsView.as_view(), name='account-settings'),
    
]



