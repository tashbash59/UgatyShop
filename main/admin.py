from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','price','stock','available','created','updated']
	list_filter = ['available','created','updated']
	list_editable = ['price','stock','available']
admin.site.register(Product, ProductAdmin)