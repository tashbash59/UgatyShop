from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

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