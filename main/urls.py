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
]