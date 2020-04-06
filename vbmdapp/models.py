from django.db import models

# Create your models here.


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    specialist_in = models.CharField(max_length=50)
    doctor_gender = models.CharField(max_length=50)
    doctor_mobile_number = models.CharField(max_length=12)
    doctor_locality = models.CharField(max_length=50)


class Patient(models.Model):
    patient_id = models.CharField(max_length=8)
    patient_name = models.CharField(max_length=50)
    patient_age = models.CharField(max_length=50)
    patient_gender = models.CharField(max_length=50)
    patient_disease = models.CharField(max_length=50)
    patient_mob_num = models.CharField(max_length=12)
    patient_mail = models.EmailField(max_length=50)
    patient_locality = models.CharField(max_length=50)
    visting_doctor_name = models.CharField(max_length=50)
