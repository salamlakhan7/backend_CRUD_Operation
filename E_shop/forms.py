from django import forms
from .models import LocalShop

class LocalShopForm(forms.ModelForm):
    class Meta:
        model = LocalShop
        fields = "__all__"