"""
    This is the URL.py file for the Recurring Charges Manager
"""
from django.urls import path
from .views import (
    ChargesListView,
    ChargesDetailView,
    ChargesCreateView,
    ChargesUpdateView,
    ChargesDeleteView,
    )
from . import views

urlpatterns = [
    path('', ChargesListView.as_view(), name='recurring-charges-manager-home'),
    path('<int:pk>/', ChargesDetailView.as_view(), name='recurring-charges-detail'),
    path('new/', ChargesCreateView.as_view(), name='recurring-charges-create'), 
    path('<int:pk>/update/', ChargesUpdateView.as_view(), name='recurring-charges-update'), 
    path('<int:pk>/delete/', ChargesDeleteView.as_view(), name='recurring-charges-delete'),
    path('about/', views.about, name='recurring-charges-manager-about'),
]