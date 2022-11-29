import re
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import BlogUser

class UserSignUpForm(UserCreationForm):
	class Meta:
		model = BlogUser
		fields = ('username', 'password1', 'password2', 'photo', 'email')
		widgets = {
			'username': forms.TextInput(attrs={
				'class': 'name form-control',
			}),
			'password1': forms.PasswordInput(attrs={
				'class': 'password form-control',
			}),
			'password2': forms.PasswordInput(attrs={
				'class': 'password form-control',
			}),
			'photo': forms.FileInput(attrs={
				'class': 'image form-control',
			}),
			'email': forms.EmailInput(attrs={
				'class': 'email form-control',
			})
		}


class UserSignInForm(AuthenticationForm):
	username = forms.CharField(label='Введите логин', widget=forms.TextInput())
	password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput())