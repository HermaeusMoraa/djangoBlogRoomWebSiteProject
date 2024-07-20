
from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUserModel
		fields = ['username', 'email', 'country', 'gender']



class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUserModel
		fields = ['username', 'email', 'country', 'gender']



class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)




