from django.shortcuts import render
from .models import recurringCharge

def home(request):
    context = {
        'recurringCharges': recurringCharge.objects.all()
    }
    return render(request, 'recurringChargesManager/home.html', context)

def about(request):
    return render(request, 'recurringChargesManager/about.html', {'title': 'About'})
