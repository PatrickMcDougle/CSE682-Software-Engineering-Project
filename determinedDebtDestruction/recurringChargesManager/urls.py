"""
    This is the URL.py file for the Recurring Charges Manager
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recurring-charges-manager-home'),
    path('about/', views.about, name='recurring-charges-manager-about'),
]