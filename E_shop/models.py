from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.
class LocalShop(models.Model):
    shop_name   = models.CharField(max_length=30)
    city        = models.CharField(max_length=10)
    category    = models.CharField(max_length=10)
    rating      = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
    is_verified = models.BooleanField(default=False)
    shop_logo   = models.ImageField(upload_to="shops/", null=True , blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.shop_name