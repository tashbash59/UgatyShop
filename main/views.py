from django.shortcuts import render, redirect
from .forms import SignUpForm, ProductForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import FormMixin



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

def T_shirt(request):
	products = Product.objects.filter(category="футболки")
	return render(request, "main/T_shirt.html", {'products':products})

def Hoody(request):
	products = Product.objects.filter(category="кофты")
	return render(request, "main/hoody.html", {'products':products})

def Other(request):
	products = Product.objects.filter(category="другое")
	return render(request, "main/other.html", {'products':products})

class About(DetailView):
	model = Product
	template_name = 'main/Product.html' 
	context_object_name = 'product'

class Edit(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'main/AdminProduct.html'
	context_object_name = 'product'


def Admin(request):
	t_shirt= Product.objects.filter(category="футболки")
	hoody = Product.objects.filter(category="кофты")
	other = Product.objects.filter(category="другое")
	return render(request, 'main/AdminMain.html', {'T_shirt':t_shirt,
												   'Hoody':hoody,
												   'Other':other})

def AddProduct(request):
	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('admin')
	form = ProductForm()
	return render(request, 'main/AdminProduct.html', {'form':form})


def Bag(request):
    return render(request, 'main/Bag.html', {'cart': Cart(request)})

def cart(request):
	pass

def Logout(request):
	logout(request)
	return redirect('main')
