from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse, HttpRequest

# builtin Auth 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout  
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

# Messages
from pyexpat.errors import messages

# Model & Forms & path 
from . models import LocalShop
from .forms import LocalShopForm 
from streamlit import form
import os

@login_required(login_url="login_view")
def create_shop(request):
    form = LocalShopForm()
    if request.method=="POST":
        form = LocalShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shop_list")
    else:
        form = LocalShopForm()
    return render (request, "create_shop_form.html",{"form":form})

def shop_list(request):
    list = LocalShop.objects.filter(rating__gte=7,is_verified=True)
    return render(request, "display_shop_list.html",{"list":list})

def signup_view(request):
    form = UserCreationForm()
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("login_view")
    return render(request,"signup.html",{"form":form})

def delete_shop(request,id):
    shop = get_object_or_404(LocalShop,id=id)
    if request.method=="POST":
        if os.path.exists(shop.shop_logo.path):
            os.remove(shop.shop_logo.path)
        shop.delete()
        messages.success(request,"you deleted")
    return redirect("shop_list")

from django.contrib import messages
def update_shop(request,id):
    shop = get_object_or_404(LocalShop,id=id)
    old_shop = shop.shop_logo
    if request.method=="POST": 
        form= LocalShopForm(request.POST, request.FILES,instance=shop)
        if form.is_valid():
            updated_shop= form.save()
            if "shop_logo" in request.FILES and old_shop:
                if old_shop.path != updated_shop.shop_logo.path:
                    if os.path.exists(old_shop.path) :
                        os.remove(old_shop.path)
            messages.success(request ,"updation done")
            return redirect("shop_list")
    else:
        form = LocalShopForm(instance=shop)
    return render(request,"create_shop_form.html",{"form":form})

def login_view(request):
    form = AuthenticationForm()
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST )
        if form.is_valid():
           user = form.get_user()
           login(request,user)
           return redirect("create_shop")
    return render(request,"login.html",{"form":form})

def logout_view(request):
    logout(request)
    messages.success(request,"you're logout")
    return redirect ("land_page")
        
def land_page(request):
    return render(request,"landing_page.html")
    