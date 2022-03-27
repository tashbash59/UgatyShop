from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def MainPage(request):
	form = SignUpForm()
	if request.method == 'POST':
		if 'reg' in request.POST:
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('main')
		else:
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request,user)
				return redirect('main')
			else:
				messages.info(request, 'Неправильный логин или пароль')
	return render(request, "main/MainPage.html", {"form":form})


def Logout(request):
	logout(request)
	return redirect('main')