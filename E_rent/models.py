from django.db import models
import datetime

from django.db import models
from django.utils import timezone

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
    