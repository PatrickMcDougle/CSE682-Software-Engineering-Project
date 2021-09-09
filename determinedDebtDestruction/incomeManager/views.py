from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Income

#Ensures that the user can not access the page without being logged in
@login_required 
def home(request):
    incomes_list = Income.objects.all()
    my_incomes = incomes_list.filter(accountHolder=request.user) #Filter incomes based on logged in user
    context = {
     'incomes': my_incomes
    }
    return render(request, 'incomeManager/home.html', context)

#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'incomeManager/about.html', {'title': 'About'})