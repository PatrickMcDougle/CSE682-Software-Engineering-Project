from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Debt

#Ensures that the user can not access the page without being logged in
@login_required 
def home(request):
    context = {
        'debts': Debt.objects.all()
    }
    return render(request, 'debtManager/home.html', context)

#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'debtManager/about.html', {'title': 'About'})