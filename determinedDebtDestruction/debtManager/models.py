from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    DEBT_TYPES = (
        ('C', 'Credit Card'),
        ('B', 'Bank Loan'),
        ('L', 'Loan Shark'),
        ('O', 'Other'),
    )
    
    nickname               = models.CharField("Debt Name:", max_length=100)
    currentDebtAmount      = models.FloatField("Current Debt Amount:")
    accountNumber          = models.PositiveIntegerField("Account Number:")
    debtType               = models.CharField("Type of Debt:", max_length=1, choices=DEBT_TYPES)
    APR                    = models.FloatField("APR:")
    paymentDate            = models.DateField("Payment Date:")
    minimumPaymentRequired = models.FloatField("Minimum Payment Amount:")
    accountHolder          = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #Attach a Debt to the user!

    def __str__(self):
        return self.nickname