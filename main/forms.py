from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, CartProduct

class SignUpForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.fields["username"].widget.attrs.update({
			'class': 'modal-body__MailInput w-100'
			})
		self.fields["email"].widget.attrs.update({
			'class': 'modal-body__MailInput w-100'
			})
		self.fields["password1"].widget.attrs.update({
			'class': 'modal-body__PasswordInput w-100'
			})
		self.fields["password2"].widget.attrs.update({
			'class': 'modal-body__PasswordInput w-100'
			})


	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['name','category',
		          'image','description',
		          'price','stock',
		          'available'
		]

		widgets = {
			"name": forms.TextInput(),
			"category": forms.Select(),
			"stock": forms.NumberInput(),
			"price": forms.NumberInput(),
			"description": forms.Textarea(),
			"image": forms.ClearableFileInput()
		}

class AddCartForm(forms.ModelForm):

	class Meta:
		model = CartProduct
		fields = ['size','count','products','created_by']

		widgets = {
			"size": forms.Select(attrs={'class':''}),
			"count": forms.NumberInput(attrs={'class':''}),
			"products": forms.HiddenInput(attrs={'class':''}),
			"created_by": forms.HiddenInput(attrs={'class':''})
		}