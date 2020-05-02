from django.urls import path
from . import views

#app_name = 'solarpvAPI'

urlpatterns = [
	path('certificates/', views.CertificateListView.as_view(), name='Certificate_List'),
	path('certificates/<pk>/', views.CertificateDetailView.as_view(), name='Certificate_Detail'),
	path('products/', views.ProductListView.as_view(), name='Product_List'),
	path('products/<pk>/', views.ProductDetailView.as_view(), name='Product_Detail'),
        path('services/', views.ServiceListView.as_view(), name='Service_List'),
        path('services/<pk>/', views.ServiceDetailView.as_view(), name='Service_Detail'),
]
