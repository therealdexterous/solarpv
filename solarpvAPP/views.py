from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .filters import *



def index(request):
	return render(request, 'solarpvAPP/index.html')

def registered_company(request):
	return render(request, 'solarpvAPP/registered_company')

def registered_user(request):
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'solarpvAPP/registered_user.html', context)

def login(request):
	return render(request, 'solarpvAPP/login.html')

def search(request):
	certs = Certificate.objects.all()
	certcount = certs.count()

	certform = CertificateForm()
	context = {'certform':certform, 'certs':certs, 'certcount':certcount}

	return render(request, 'solarpvAPP/search.html', context)

def clientportal(request):
	return render(request, 'solarpvAPP/clientportal.html')

def staffportal(request):
	return render(request, 'solarpvAPP/staffportal.html')

def api(request):
	return render(request, 'solarpvAPP/api.html')
