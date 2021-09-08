from django.shortcuts import render
from .models import Income

def home(request):
    context = {
        'incomes': Income.objects.all()
    }
    return render(request, 'incomeManager/home.html', context)

def about(request):
    return render(request, 'incomeManager/about.html', {'title': 'About'})