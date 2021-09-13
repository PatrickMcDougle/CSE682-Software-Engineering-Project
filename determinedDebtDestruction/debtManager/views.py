from django.shortcuts import render

def about(request):
    return render(request, 'debtManager/about.html', {'title': 'About'})