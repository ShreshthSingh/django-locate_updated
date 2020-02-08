from django.db import models

# Create your models here.
class Student(models.Model):
    name =  models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    floorno = models.IntegerField(max_length=5)
    roomno = models.IntegerField(max_length=10)

