from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('industries/', views.IndustriesView.as_view(), name='industries'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
