

# Create your models here.
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Students(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
