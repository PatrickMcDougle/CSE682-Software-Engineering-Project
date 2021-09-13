from django.db import models
from django.contrib.auth.models import User


#change test from jamie
class Debt(models.Model):
    PAY_FREQUENCIES = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('B', 'Bi-Weekly'),
        ('S', 'Semi-Monthly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )
    PAY_DAYS = (
        ('M', 'Monday'),
        ('T', 'Tuesday'),
        ('W', 'Wednesday'),
        ('R', 'Thursday'),
        ('F', 'Friday'),
    )
    DEBT_TYPES = (
        ('CC', 'Credit Card'),
        ('BL', 'Bank Loan'),
        ('LS', 'Loan Shark'),
        ('M',  'Mortgage'),
        ('CL', 'Car Loan'),
    )

    name = models.CharField("Debt Nickname:", max_length=100)
    accountNumber = models.CharField("Account Number", max_length=100)
    debtType = models.CharField("Debt Type:", max_length=2, choices=DEBT_TYPES)
    debtCompany = models.CharField("Company Name:", max_length=100)
    debtCompanyAddress = models.CharField("Company Address:", max_length=100)
    apr = models.FloatField("APR")
    dueDate = models.DateField("Due Date")
    payAmount = models.FloatField("Minimum Payment Amount")
    payDay = models.CharField('Payday:', max_length=1, choices=PAY_DAYS)
    accountHolder = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #Attach an Income to the user!
    

    def __str__(self):
        return self.name
