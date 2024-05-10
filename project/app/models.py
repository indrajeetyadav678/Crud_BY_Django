from django.db import models

# Create your models here.
class EmplayeeModel(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Number=models.CharField(max_length=10)
    Position=models.CharField(max_length=30)
    Sallary=models.IntegerField()
    
