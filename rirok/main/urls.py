from django.urls import path 
from main import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('base/', views.base, name = 'base'),
    path('service/', views.service, name = 'service'),
    path('contact/', views.contact, name = 'contact'),
]
