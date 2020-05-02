from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registered_user/', views.registered_user, name='reg'),
    path('registered_company/', views.registered_company, name='company'),
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('api/', views.api, name='api'),
    path('api/', include('solarpvAPP.api.urls')),
    path('clientportal/', views.clientportal, name='clientportal'),
    path('staffportal/', views.staffportal, name='staffportal'),
]
