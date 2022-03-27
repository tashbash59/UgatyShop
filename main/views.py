from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

def MainPage(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main')
	return render(request, "main/MainPage.html", {"form":form})


def Logout(request):
	logout(request)
	return redirect('main')