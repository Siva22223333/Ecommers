from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Useraccount(models.Model):
    name=models.CharField(max_length=50, null=True)
    mobileno=models.CharField(max_length=40, null=True)
    email=models.EmailField(max_length=254, null=True,unique=True)
    password=models.CharField( max_length=550)
    address=models.CharField( max_length=150, null=True)
    token=models.CharField(max_length=150, null=True)
