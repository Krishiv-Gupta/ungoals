from django.db import models

# Create your models here.
class e(models.Model):
    Name=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    W=models.CharField(max_length=500)

class goal(models.Model):
    Name=models.CharField(max_length=50)
    Text=models.CharField(max_length=500)
    Photo=models.CharField(max_length=500)
    