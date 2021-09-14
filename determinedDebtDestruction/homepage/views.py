from django.shortcuts import render
from django.http import HttpResponse
from django.apps import apps
Income = apps.get_model('incomeManager', 'Income') #Import the Income Model from incomeManager App
Debt = apps.get_model('debtManager', 'Debt') #Import the Debt Model from debtManager App
RecurringCharge = apps.get_model('recurringChargesManager', 'recurringCharge') #Import the RecurringCharge Model from debtManager App

def home(request):
    if request.user.is_authenticated:
        incomes_list = Income.objects.all()
        my_incomes = incomes_list.filter(accountHolder=request.user) #Filter incomes based on logged in user
        incomeAmount = 0
        for income in my_incomes:
            incomeAmount += income.payAmount
        
        debts_list = Debt.objects.all()
        my_debts = debts_list.filter(accountHolder=request.user) #Filter incomes based on logged in user
        debtAmount = 0
        for debt in my_debts:
            debtAmount += debt.currentDebtAmount
        
        
        charges_list = RecurringCharge.objects.all()
        my_charges = charges_list.filter(accountHolder=request.user) #Filter recurringCharges based on logged in user
        chargeAmount = 0
        for charge in my_charges:
            chargeAmount += charge.payAmount
        
        context = {
            'incomeTotal': incomeAmount,
            'debtTotal': debtAmount,
            'chargeTotal': chargeAmount
        }
        return render(request, 'homepage/homepage.html', context)
    else:
        context = {
            'incomeTotal': 0,
            'debtTotal': 0,
            'chargeTotal': 0
        }
        return render(request, 'homepage/homepage.html', context)

def about(request):
    return render(request, 'homepage/about.html')