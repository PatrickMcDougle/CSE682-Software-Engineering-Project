"""
    This is the URL.py file for the Income Manager
"""
from django.urls import path
from .views import (
    IncomeListView,
    IncomeDetailView,
    IncomeCreateView,
    IncomeUpdateView,
    IncomeDeleteView,
    )
from . import views

'''path('', views.home, name='income-manager-home'),'''

urlpatterns = [
    path('', IncomeListView.as_view(), name='income-manager-home'),
    path('<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),
    path('new/', IncomeCreateView.as_view(), name='income-create'), 
    path('<int:pk>/update/', IncomeUpdateView.as_view(), name='income-update'), 
    path('<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),  
    path('about/', views.about, name='income-manager-about'),
]