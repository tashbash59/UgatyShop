from django.urls import path
from django.contrib import admin
from main import views
from .views import *

urlpatterns = [
	path('', views.MainPage, name = 'main'),
	path('logout', views.Logout, name = 'logout'),
	path('bag/', views.Bag, name = 'bag'),
]