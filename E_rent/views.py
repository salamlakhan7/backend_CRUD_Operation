from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest,HttpResponse
from streamlit import form

# Create your views here.
from .models import Ghotki_Ecommerce, Salam
from .forms import Ghotki_EcommerceForm, SalamForm

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
