from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def authentication(request):
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
	return form


def MainPage(request):
	form = authentication(request)
	return render(request, "main/MainPage.html", {"form":form})

def Bag(request):
	return render(request, "main/Bag.html", {})

def T_shirt(request):
	products = Product.objects.filter(available=True,category="футболки")
	return render(request, "main/T_shirt.html", {'products':products})

def Hoody(request):
	products = Product.objects.filter(available=True,category="кофты")
	return render(request, "main/hoody.html", {'products':products})

def Other(request):
	products = Product.objects.filter(available=True,category="другое")
	return render(request, "main/other.html", {'products':products})


def Logout(request):
	logout(request)
	return redirect('main')