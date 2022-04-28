from django.shortcuts import render, redirect, reverse 
from .forms import SignUpForm, ProductForm,AddCartForm
from .models import Product, CartProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, FormView
from django.views.generic.edit import FormMixin
from django.db.models import Sum


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

class About(FormMixin, DetailView):
    model = Product
    template_name = 'main/Product.html' 
    context_object_name = 'product'
    form_class = AddCartForm

    def get_success_url(self):
        return reverse('about', kwargs={'pk': self.object.id} )

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['form'] = AddCartForm(initial={'products': self.object,'created_by': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print('invalid')
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(About, self).form_valid(form)


class Edit(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/AdminProduct.html'
    context_object_name = 'product'
    def get_success_url(self):
        return reverse('admin')

def Admin(request):
    t_shirt= Product.objects.filter(category="футболки")
    hoody = Product.objects.filter(category="кофты")
    other = Product.objects.filter(category="другое")
    return render(request, 'main/AdminMain.html', {'T_shirt':t_shirt,
                                                   'Hoody':hoody,
                                                   'Other':other})

def Delete(request,id):
    dlt= CartProduct.objects.get(id=id)
    dlt.delete()
    return redirect('bag')

def AddProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data['name'])
            print(form.cleaned_data['price'])
            print(form.cleaned_data['description'])
            print(form.cleaned_data['image'])
            return redirect('admin')
    form = ProductForm()
    return render(request, 'main/AdminProduct.html', {'form':form})


def Bag(request):
    tovar = CartProduct.objects.filter(created_by=request.user)
    if request.method == 'POST':
        delete = CartProduct.objects.get(id=tovar.id)
        delete.delete()

    #total_price = tovar.aggregate(Sum('productprice'))
    return render(request, 'main/Bag.html', {"tovar":tovar})

def cart(request):
    pass

def Logout(request):
    logout(request)
    return redirect('main')
