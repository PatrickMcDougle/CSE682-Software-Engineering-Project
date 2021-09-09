"""
    This is the URL.py file for the Debt Manager
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='debt-manager-home'),
    path('about/', views.about, name='debt-manager-about'),
]