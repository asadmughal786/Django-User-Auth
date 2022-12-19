from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    password1= forms.CharField(label="Password",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name','password1','password2']
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name': 'Last Name', 'email':'Email Address'}


class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}


class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields ='__all__'
        labels = {'email':'Email'}
