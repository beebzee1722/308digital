from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('pages/home/', views.HomeView.as_view(), name='home'),
    path('pages/services/', views.ServicesView.as_view(), name='services'),
    path('pages/industries/', views.IndustriesView.as_view(), name='industries'),
    path('pages/about/', views.AboutView.as_view(), name='about'),
    path('pages/contact/', views.ContactView.as_view(), name='contact'),
    path('api/contact/', views.contact_submit, name='contact_submit'),
]
