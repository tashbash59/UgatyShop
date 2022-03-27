from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args,**kwargs)
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
		fields = ['email', 'password1', 'password2']


