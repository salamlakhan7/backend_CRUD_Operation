
from django import forms
from .models import Ghotki_Ecommerce, Salam

class Ghotki_EcommerceForm(forms.ModelForm):
    class Meta:
        model = Ghotki_Ecommerce
        fields=["store_name","store_location","Store_type","store_rate","store_description","store_status"]
        
        
class SalamForm(forms.ModelForm):
    class Meta:
        model = Salam
        fields = ["name","stack","experience"]
    
    def clean_experience(self):
        experience = self.cleaned_data.get("experience")
        if experience < 1 or experience > 5:
            raise forms.ValidationError("Experience must be between 1 and 5.")
        return experience