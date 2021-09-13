# Generated by Django 3.2.7 on 2021-09-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Income Source:')),
                ('payFrequency', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('B', 'Bi-Weekly'), ('S', 'Semi-Monthly'), ('M', 'Monthly'), ('Y', 'Yearly')], max_length=1, verbose_name='Frequency of Pay:')),
                ('payAmount', models.FloatField()),
                ('payDay', models.CharField(choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('R', 'Thursday'), ('F', 'Friday')], max_length=1, verbose_name='Payday:')),
            ],
        ),
    ]
