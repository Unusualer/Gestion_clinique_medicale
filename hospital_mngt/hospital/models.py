from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.IntegerField()
    SP = models.CharField(max_length=50)
    email = models.EmailField(max_length=240,null=True)
    password = models.CharField(max_length=50,null=True)
    type_personnel = "doctor"
    
    def __str__(self):
        return self.Name

class Nurse(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.IntegerField()
    SP = models.CharField(max_length=50)
    email = models.EmailField(max_length=240,null=True)
    password = models.CharField(max_length=50,null=True)
    type_personnel = "nurse"
    
class Patient(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(null = True)
    Address = models.TextField()
    Maladie = models.TextField(null=True)
    email = models.EmailField(max_length=240,null=True)
    password = models.CharField(max_length=50,null=True)
    type_personnel = "patient"

class Appointment(models.Model):
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date = models.DateField()
    time = models.TimeField()
    
    