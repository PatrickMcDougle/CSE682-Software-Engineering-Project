from django.db import models
from django.contrib.auth.models import User

class recurringCharge(models.Model):
    PAY_FREQUENCIES = (
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('B', 'Bi-Weekly'),
        ('S', 'Semi-Monthly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    )
    
    name          = models.CharField("Reccuring Charge:", max_length=100)
    payDueDate    = models.DateField("Payment Due Date:")
    payAmount     = models.FloatField()
    paySchedule   = models.CharField("Frequency of Payments:", max_length=1, choices=PAY_FREQUENCIES)
    accountHolder = models.ForeignKey(User, on_delete=models.CASCADE, null=True) #Attach a Recurring Charge to the user!

    def __str__(self):
        return self.name
    
    def determineMonthlyCharge(self):
        if(self.paySchedule == 'D'):   #Paid Daily
            monthlyIncome = self.payAmount * 30 #Default assume 30 days in Month
        elif(self.paySchedule == 'W'): #Paid Weekly
            monthlyIncome = self.payAmount * 4 #Four weeks in a month
        elif(self.paySchedule == 'B'): #Paid Bi-weekly
            monthlyIncome = self.payAmount * 2 #Paid Twice a month
        elif(self.paySchedule == 'S'): #Paid Semi-Monthly
            monthlyIncome = self.payAmount #Need to talk with team on this one....
        elif(self.paySchedule == 'Y'): #Paid Yearly
            monthlyIncome = self.payAmount / 12 #12 Months in a year
        else: #Paid Monthly
            monthlyIncome = self.payAmount
        return monthlyIncome