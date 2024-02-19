from django.db import models

from django.db import models
import time

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    message = models.TextField()

from django.db import models
from django.contrib.auth.models import User



class DoctorT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.user.get_full_name()
    
class PatientT(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=12)
    contact = models.CharField(max_length=10)
    def __str__(self):
        return self.user.get_full_name()

class AppointT(models.Model):
    doctor = models.ForeignKey(DoctorT, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientT, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.TimeField(default=time.timezone)

    def __str__(self):
        return f"Appointment: {self.doctor.user} with {self.patient.user} on {self.date}"
    
class AppointCopy(models.Model):
    doctor_name = models.CharField(max_length=30)
    patient_name = models.CharField(max_length=30)
    date = models.DateTimeField()
    time = models.TimeField(default=time.timezone)