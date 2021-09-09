"""
    This is the URL.py file for the Income Manager
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='income-manager-home'),
    path('about/', views.about, name='income-manager-about'),
]