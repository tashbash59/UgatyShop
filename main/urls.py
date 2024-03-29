from django.urls import path
from django.contrib import admin
from main import views
from .views import *

urlpatterns = [
	path('', views.MainPage, name = 'main'),
	path('logout', views.Logout, name = 'logout'),
	path('bag/', views.Bag, name = 'bag'),
	path('t-shirt/', views.T_shirt, name = 't_shirt'),
	path('hoody/', views.Hoody, name = 'hoody'),
	path('other/', views.Other, name = 'other'),
	path('about/<int:pk>', views.About.as_view(), name = 'about'),
	path('admin1/addproduct/', views.AddProduct, name='add'),
	path('admin1/edit/<int:pk>', views.Edit.as_view(), name='edit'),
	path('admin1/', views.Admin, name='admin')
]