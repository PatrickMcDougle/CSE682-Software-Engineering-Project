from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import recurringCharge

#Ensures that the user can not access the page without being logged in
@login_required 
def home(request):
    charges_list = recurringCharge.objects.all()
    my_charges = charges_list.filter(accountHolder=request.user) #Filter recurringCharges based on logged in user
    context = {
        'recurringCharges': my_charges
    }
    return render(request, 'recurringChargesManager/home.html', context)
 
class ChargesListView(LoginRequiredMixin, ListView):
    model = recurringCharge
    template_name = 'recurringChargesManager/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'recurringCharges'
    ordering = ['-payAmount'] #Sort from largest paying to smallest paying
    paginate_by = 5 #How many recurringCharges to display 
    def get_queryset(self):
        return recurringCharge.objects.filter(accountHolder=self.request.user).order_by('-payAmount')
        
class ChargesDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = recurringCharge
    
    #Check if current user is accountHolder of the Income to update
    def test_func(self):
        recurringCharge = self.get_object()
        if self.request.user == recurringCharge.accountHolder:
            return True
        return False

class ChargesCreateView(LoginRequiredMixin, CreateView):
    model = recurringCharge
    fields = ['name', 'payDueDate', 'payAmount', 'paySchedule']
    success_url = '/charges' #Where to redirect the form after successful submission
    def form_valid(self, form):
        form.instance.accountHolder = self.request.user
        return super().form_valid(form)

class ChargesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = recurringCharge
    fields = ['name', 'payDueDate', 'payAmount', 'paySchedule']
    success_url = '/charges' #Where to redirect the form after successful submission
    def form_valid(self, form):
        form.instance.accountHolder = self.request.user
        return super().form_valid(form)

    #Check if current user is accountHolder of the Income to update
    def test_func(self):
        charge = self.get_object()
        if self.request.user == charge.accountHolder:
            return True
        return False
        
class ChargesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = recurringCharge
    success_url = '/charges' #Where to redirect the form after successful deletion
    
    #Check if current user is accountHolder of the Income delete
    def test_func(self):
        charge = self.get_object()
        if self.request.user == charge.accountHolder:
            return True
        return False
        
#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'recurringChargesManager/about.html', {'title': 'About'})
