from django.contrib import admin

# Register your models here.
from . models import Ghotki_Ecommerce, Salam


class SalamAdmin(admin.ModelAdmin):
    fields = ["name", "stack", "experience"]
    
admin.site.register(Ghotki_Ecommerce)
admin.site.register(Salam, SalamAdmin)