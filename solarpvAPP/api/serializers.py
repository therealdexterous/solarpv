from rest_framework import serializers
from ..models import *

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['Model_Number', 'Product_Name', 'Slug']

class CertificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Certificate
		fields = ['Certificate_Number', 'User_ID', 'Issue_Date', 'Slug']

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = ['Service_ID', 'Service_Name', 'Slug']
