
from django import forms
from .models import Ghotki_Ecommerce

class Ghotki_EcommerceForm(forms.ModelForm):
    class Meta:
        model = Ghotki_Ecommerce
        fields=["store_name","store_location","Store_type","store_rate","store_description","store_status"]
        
        
   