
from django import forms
from .models import CustomUserAccountModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = CustomUserAccountModel
		fields = ['username', 'email']



class CustomUserAccountChangeForm(UserChangeForm):
	class Meta:
		model = CustomUserAccountModel
		fields = ['username', 'email']



class CustomUserProfileChangeForm(UserChangeForm):
	class Meta:
		model = CustomUserAccountModel
		fields = [
			# 'avatar',
			# 'background',
			'first_name',
			'last_name',
			'gender',
			'date_of_birth',
			'country',
			'about'
		]




class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)




