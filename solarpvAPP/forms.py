from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.contrib.auth.models import User

class CertificateForm(ModelForm):
	class Meta:
		model = Certificate
		fields = '__all__'

class ProductsForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class ServicesForm(ModelForm):
	class Meta:
		model = Service
		fields = '__all__'

class CreateUserForm(ModelForm):
	class Meta:
		model = Registered_User
		fields = ['userID', 'password', 'clientID', 'first_name', 'middle_name', 'last_name', 'job_title', 'email_address', 'office_phone', 'cell_phone', 'prefix']

