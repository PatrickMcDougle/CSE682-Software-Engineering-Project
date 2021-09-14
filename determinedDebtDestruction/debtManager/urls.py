"""
    This is the URL.py file for the Debt Manager
"""
from django.urls import path
from .views import (
    DebtListView,
    DebtDetailView,
    DebtCreateView,
    DebtUpdateView,
    DebtDeleteView,
    )
from . import views

urlpatterns = [
    path('', DebtListView.as_view(), name='debt-manager-home'),
    path('<int:pk>/', DebtDetailView.as_view(), name='debt-detail'),
    path('new/', DebtCreateView.as_view(), name='debt-create'), 
    path('<int:pk>/update/', DebtUpdateView.as_view(), name='debt-update'), 
    path('<int:pk>/delete/', DebtDeleteView.as_view(), name='debt-delete'),  
    path('about/', views.about, name='debt-manager-about'),
]