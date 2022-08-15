from django.db import models

# Create your models here.

class Usermodel(models.Model):
    username=models.CharField(max_length=100)
    usermail=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    maritialstatus=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    class Meta:
        db_table='userreg'


