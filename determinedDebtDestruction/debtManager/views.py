from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Debt

#Ensures that the user can not access the page without being logged in
@login_required 
def home(request):
    debts_list = Debt.objects.all()
    my_debts = debts_list.filter(accountHolder=request.user) #Filter incomes based on logged in user
    context = {
        'debts': my_debts
    }
    return render(request, 'debtManager/home.html', context)

#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'debtManager/about.html', {'title': 'About'})