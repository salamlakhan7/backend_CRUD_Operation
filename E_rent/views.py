import os
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest,HttpResponse
from streamlit import form

# Create your views here.
from .models import Ghotki_Ecommerce, RestaurantProfile, Salam, Salamoffices ,RestaurantProfile
from .forms import Ghotki_EcommerceForm, RestaurantProfileForm, SalamForm, SalamofficesForm

def create_form(request):
    form = Ghotki_EcommerceForm()
    if request.method=="POST":
        form= Ghotki_EcommerceForm(request.POST)
        if form.is_valid():
            form.save()
            form=Ghotki_EcommerceForm()
    else:
        form=Ghotki_EcommerceForm()
    return render(request, "create_e_form.html",{"form":form})
    
def display_store_list(request):
    lists = Ghotki_Ecommerce.objects.filter(store_status=True, store_rate__gte=5)
    #return render(request,"display_store_list.html",{"lists":lists})
    return render(request,"delete_store.html",{"lists":lists})

def delete_store(request, id):
    store = get_object_or_404(Ghotki_Ecommerce, id=id)
    if request.method == "POST":
        store.delete()
        return redirect("display_store_list")


def update_store_info(request, id):
    store = get_object_or_404(Ghotki_Ecommerce, id=id)

    if request.method == "POST":
        form = Ghotki_EcommerceForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect("display_store_list")
    else:
        form = Ghotki_EcommerceForm(instance=store)

    return render(request, "update_store_info.html", {"form": form})

    ######################## Part 2 #########################################
    
def salam_form(request):
    form = SalamForm()
    if request.method=="POST":
        form = SalamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("salam_form")
    else:
        form = SalamForm()
    return render(request ,"salam_form.html",{"form":form})

def display_salam(request):
    salam = Salam.objects.filter(experience__gte=1) 
    return render(request , "display_salam_list.html", {"salam":salam})

def delete_salam(request,id):
    salam = get_object_or_404(Salam,id=id)
    if request.method=="POST":
        salam.delete()
        messages.success(request, "Salam deleted successfully")
        return redirect("display_salam")
    
from django.contrib import messages  
def update_salam_form(request,id):
    salam = get_object_or_404(Salam , id=id)
    if request.method=="POST":
        form = SalamForm(request.POST,instance=salam)
        if form.is_valid():
            form.save()
            messages.success(request, "Salam updated successfully")
            return redirect("display_salam")
    else:
        form = SalamForm(instance=salam )
    return render(request ,"update_salam_form.html",{"form":form})

######################### part 3 ########################################

def Dis_Salamoffice_form(request):
    offices = Salamoffices.objects.filter(office_workers__gte=20 ,active_offices=True)
    return render(request ,"Dis_Salamoffice_form.html",{"offices":offices})

def Salamoffice_form(request):
    form = SalamofficesForm()
    if request.method=="POST":
        form = SalamofficesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = SalamofficesForm()
    else:
        form = SalamofficesForm()
    return render(request,"Salamoffice_form.html", {"form":form})


def del_salamoffice(request,id):
    offices  = get_object_or_404(Salamoffices , id=id)
    if request.method=="POST":
        if os.path.exists(offices.office_image.path):
           os.remove(offices.office_image.path)
        offices.delete()
        messages.success(request,"Delecte Action perofrmed successfully")
        return redirect ("Dis_Salamoffice_form")
    
    
def update_Salamoffice_form(request,id):
    offices = get_object_or_404(Salamoffices,id=id)
    old_image = offices.office_image
    if request.method=="POST":
        form = SalamofficesForm(request.POST,request.FILES,instance=offices)
        if form.is_valid():
            updated_office = form.save()
            
            # if new image uploaded, delete old one
            if "office_image" in request.FILES and old_image:
                if old_image.path != updated_office.office_image.path:
                    if os.path.exists(old_image.path):
                        os.remove(old_image.path)
                        
            messages.success(request,"Update Action Performed")
            return redirect("Dis_Salamoffice_form")
    else:
        form = SalamofficesForm(instance=offices)
    return render(request,"Salamoffice_form.html", {"form":form})

from django.contrib.auth.decorators import login_required
@login_required
def List_Restaurants(request):
    lists = RestaurantProfile.objects.filter(is_open=True, rating__gte=7)
    return render (request , "list_restaurants.html",{"lists":lists})

def form_Restaurants(request):
    form = RestaurantProfileForm()
    if request.method=="POST":
        form = RestaurantProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = RestaurantProfileForm()
    else:
        form = RestaurantProfileForm()
    return render (request, "form_restaurants.html",{"form":form})


def delelte_resturants(request,id):
    lists = get_object_or_404(RestaurantProfile,id=id)
    if request.method =="POST":
        if os.path.exists(lists.logo.path):
            os.remove(lists.logo.path)
        lists.delete()
        messages.success(request,"delete done")
    return redirect("List_Restaurants")

def update_resturants(request, id):
    lists = get_object_or_404(RestaurantProfile, id=id)
    old_logo = lists.logo
    if request.method == "POST":
        form = RestaurantProfileForm(request.POST, request.FILES, instance=lists)
        if form.is_valid():
            updated = form.save()
            # delete old logo only if new one uploaded
            if "logo" in request.FILES and old_logo:
                if old_logo.path != updated.logo.path:
                    if os.path.exists(old_logo.path):
                        os.remove(old_logo.path)
            messages.success(request, "update done")
            return redirect("List_Restaurants")

    else:
        form = RestaurantProfileForm(instance=lists)
    return render(request, "form_restaurants.html", {"form": form})

##################### Authentication ###################################
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout 
from django.contrib.auth.decorators import login_required

def signup_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # auto login after signup
            messages.success(request, "Account created successfully!")
            return redirect("List_Restaurants")
    return render(request, "Auth/signup.html", {"form": form})
        
def login_view(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST )
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"login successfully")
            return redirect("List_Restaurants")
    return render(request , "Auth/login.html",{"form":form})
            
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("login")
          
        
            
                   
        