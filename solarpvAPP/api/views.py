from rest_framework import generics
from django.shortcuts import render
from ..models import *
from .serializers import *

def api(request):
        return render(request, 'solarpvAPP/api.html')

class CertificateListView(generics.ListAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

class CertificateDetailView(generics.RetrieveAPIView):
	queryset = Certificate.objects.all()
	serializer_class = CertificateSerializer

class ProductListView(generics.ListAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer

class ServiceListView(generics.ListAPIView):
        queryset = Service.objects.all()
        serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView):
        queryset = Service.objects.all()
        serializer_class = ServiceSerializer
