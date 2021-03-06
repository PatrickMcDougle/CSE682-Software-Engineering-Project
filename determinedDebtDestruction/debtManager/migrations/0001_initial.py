# Generated by Django 3.2.7 on 2021-09-09 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100, verbose_name='Debt Name:')),
                ('currentDebtAmount', models.FloatField(verbose_name='Current Debt Amount:')),
                ('accountNumber', models.PositiveIntegerField(verbose_name='Account Number:')),
                ('debtType', models.CharField(choices=[('C', 'Credit Card'), ('B', 'Bank Loan'), ('L', 'Loan Shark'), ('O', 'Other')], max_length=1, verbose_name='Type of Debt:')),
                ('APR', models.FloatField(verbose_name='APR:')),
                ('paymentDate', models.DateField(verbose_name='Payment Date:')),
                ('minimumPaymentRequired', models.FloatField(verbose_name='Minimum Payment Amount:')),
                ('accountHolder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
