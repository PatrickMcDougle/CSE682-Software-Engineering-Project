from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import recurringCharge

#Ensures that the user can not access the page without being logged in
@login_required 
def home(request):
    context = {
        'recurringCharges': recurringCharge.objects.all()
    }
    return render(request, 'recurringChargesManager/home.html', context)

#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'recurringChargesManager/about.html', {'title': 'About'})
