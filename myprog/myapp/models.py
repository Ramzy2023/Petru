from django.db import models

# Create your models here.

class Division(models.Model):
    division_name = models.CharField(max_length=100, verbose_name="Division")

class Office(models.Model):
    office_name = models.CharField(max_length=100, verbose_name="Office")
    division = models.ForeignKey(Division,on_delete=models.CASCADE)

class Position(models.Model):
    position_name = models.CharField(max_length=100, verbose_name="Position")

class Employee(models.Model):
    employee_name = models.CharField(max_length=100, verbose_name="Employee Name")
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    office = models.ForeignKey(Office,on_delete=models.CASCADE)

class NatureOfTravel(models.Model):
    nature_travel_name = models.CharField(max_length=100,verbose_name="Nature of Travel")

class TravelOrder(models.Model):
    travel_number = models.CharField(max_length=100, verbose_name="Travel Order Number")
    destination = models.CharField(max_length=100,verbose_name="Destination")
    date_start = models.DateField(verbose_name="Date Start")
    date_end = models.DateField(verbose_name="Date End")
    purpose = models.CharField(max_length=100,verbose_name="Purpose of Travel")
    natureoftavel = models.ForeignKey(NatureOfTravel,on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/', default='documents/default_file.pdf', verbose_name="Upload File")

class AssignTravel(models.Model):
    travelorder = models.ForeignKey(TravelOrder,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
