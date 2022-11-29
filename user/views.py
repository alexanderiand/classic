from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserSignUpForm, UserSignInForm

# Create your views here.
def user_sign_up(request):
	"""sign up user"""
	if request.method == 'POST':
		form = UserSignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Вы успешно зарегистрировались!')
			login(request, user)
			return redirect('main')
		else:
			messages.error(request, 'Ошибка регистрации, введите корректные данные!')
	else:
		form = UserSignUpForm()
	return render(request, 'sign_up.html', {
		'form': form,
	})

def user_sign_in(request):
	"""login"""
	if request.method == 'POST':
		form = UserSignInForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, f'{user.username}, добро пожаловать!')
			return redirect('main')
		else:
			messages.error(request, 'Ошибка авторизации, введите данные корректно!')
	else:
		form = UserSignInForm()
	return render(request, 'sign_in.html', {
		'form': form,
	})


def user_logout(request):
	"""user logit"""
	logout(request)
	messages.success(request, 'Досвидули, заходи ещё!)')
	return redirect('main')
