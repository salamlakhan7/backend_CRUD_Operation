from django.contrib import admin

# Register your models here.
from . models import Ghotki_Ecommerce, Salam, Salamoffices , RestaurantProfile 


class SalamAdmin(admin.ModelAdmin):
    fields = ["name", "stack", "experience"]
    
admin.site.register(Ghotki_Ecommerce)
admin.site.register(Salam, SalamAdmin)
admin.site.register(Salamoffices)
admin.site.register(RestaurantProfile)