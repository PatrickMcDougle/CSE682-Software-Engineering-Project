from django.shortcuts import render
from .models import Debt

def home(request):
    context = {
        'debts': Debt.objects.all()
    }
    return render(request, 'debtManager/home.html', context)

def about(request):
    return render(request, 'debtManager/about.html', {'title': 'About'})