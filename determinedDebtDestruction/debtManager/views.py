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

class DebtListView(LoginRequiredMixin, ListView):
    model = Debt
    template_name = 'debtManager/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'debts'
    ordering = ['-currentDebtAmount'] #Sort from largest debt to smallest debt
    paginate_by = 5 #How many incomes to display 
    def get_queryset(self):
        return Debt.objects.filter(accountHolder=self.request.user).order_by('-currentDebtAmount')
        
class DebtDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Debt
    
    #Check if current user is accountHolder of the Debt to update
    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.accountHolder:
            return True
        return False

class DebtCreateView(LoginRequiredMixin, CreateView):
    model = Debt
    fields = ['nickname', 'currentDebtAmount', 'accountNumber', 'debtType', 'APR', 'paymentDate', 'minimumPaymentRequired']
    success_url = '/debt' #Where to redirect the form after successful submission
    def form_valid(self, form):
        form.instance.accountHolder = self.request.user
        return super().form_valid(form)

class DebtUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Debt
    fields = ['nickname', 'currentDebtAmount', 'accountNumber', 'debtType', 'APR', 'paymentDate', 'minimumPaymentRequired']
    success_url = '/debt' #Where to redirect the form after successful submission
    def form_valid(self, form):
        form.instance.accountHolder = self.request.user
        return super().form_valid(form)

    #Check if current user is accountHolder of the Income to update
    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.accountHolder:
            return True
        return False
        
class DebtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Debt
    success_url = '/debt' #Where to redirect the form after successful deletion
    
    #Check if current user is accountHolder of the Income delete
    def test_func(self):
        debt = self.get_object()
        if self.request.user == debt.accountHolder:
            return True
        return False
        
#Ensures that the user can not access the page without being logged in
@login_required 
def about(request):
    return render(request, 'debtManager/about.html', {'title': 'About'})