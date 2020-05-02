import django_filters

from .models import *

class CertificateFilter(django_filters.FilterSet):
	class Meta:
		model = Certificate
		fields = '__all__'
