# Generated by Django 5.1.3 on 2024-11-08 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_name', models.CharField(max_length=100, verbose_name='Division')),
            ],
        ),
        migrations.CreateModel(
            name='NatureOfTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature_travel_name', models.CharField(max_length=100, verbose_name='Nature of Travel')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=100, verbose_name='Position')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=100, verbose_name='Office')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.division')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.office')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.position')),
            ],
        ),
        migrations.CreateModel(
            name='TravelOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_number', models.CharField(max_length=100, verbose_name='Travel Order Number')),
                ('destination', models.CharField(max_length=100, verbose_name='Destination')),
                ('date_start', models.DateField(verbose_name='Date Start')),
                ('date_end', models.DateField(verbose_name='Date End')),
                ('purpose', models.CharField(max_length=100, verbose_name='Purpose of Travel')),
                ('natureoftavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.natureoftravel')),
            ],
        ),
        migrations.CreateModel(
            name='AssignTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
                ('travelorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.travelorder')),
            ],
        ),
    ]
