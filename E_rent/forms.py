
from django import forms
from .models import Ghotki_Ecommerce, RestaurantProfile, Salam , Salamoffices

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
    
class SalamofficesForm(forms.ModelForm):
    class Meta:
        model = Salamoffices
       # fields = ["office_name","office_location","office_workers","active_offices"]
        fields = "__all__"
        
class RestaurantProfileForm(forms.ModelForm):
    class Meta:
        model = RestaurantProfile
        fields = "__all__"