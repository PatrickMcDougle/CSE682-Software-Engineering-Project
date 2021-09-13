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

class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'incomeManager/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'incomes'
    ordering = ['-payAmount'] #Sort from largest paying to smallest paying
    paginate_by = 5 #How many incomes to display 
    def get_queryset(self):
        return Income.objects.filter(accountHolder=self.request.user).order_by('-payAmount')
        
class IncomeDetailView(LoginRequiredMixin, DetailView):
    model = Income

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    fields = ['name', 'payFrequency', 'payAmount', 'payDay']
    success_url = '/income' #Where to redirect the form after successful submission
    def form_valid(self, form):
        form.instance.accountHolder = self.request.user
        return super().form_valid(form)

class IncomeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Income
    fields = ['name', 'payFrequency', 'payAmount', 'payDay']
    success_url = '/income' #Where to redirect the form after successful submission
    def form_valid(self, form):
        form.instance.accountHolder = self.request.user
        return super().form_valid(form)

    #Check if current user is accountHolder of the Income to update
    def test_func(self):
        income = self.get_object()
        if self.request.user == income.accountHolder:
            return True
        return False
        
class IncomeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Income
    success_url = '/income' #Where to redirect the form after successful deletion
    
    #Check if current user is accountHolder of the Income delete
    def test_func(self):
        income = self.get_object()
        if self.request.user == income.accountHolder:
            return True
        return False
    
#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'incomeManager/about.html', {'title': 'About'})