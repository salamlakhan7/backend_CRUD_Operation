from django.db import models
import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Ghotki_Ecommerce(models.Model):
    store_name = models.CharField(max_length=20)
    store_location= models.CharField(max_length=20)
    Store_type= models.CharField(max_length=10)
    store_rate=models.IntegerField()
    store_description= models.TextField(max_length=200)
    store_status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.store_name
    ######################### Part 2 #########################################
    
class Salam(models.Model):
    name = models.CharField(max_length=10)
    stack = models.CharField(max_length=10)
    #experience = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    experience = models.IntegerField()
    def __str__(self):
        return self.name
    
    
######################### part 3 ##################################

class Salamoffices(models.Model):
    office_name = models.CharField(max_length=20)
    office_location = models.CharField(max_length=30)
    office_workers = models.IntegerField(validators=[MinValueValidator(20),MaxValueValidator(50)])
    active_offices = models.BooleanField(default=False)
    
    def __str__(self):
        return self.office_name 
    