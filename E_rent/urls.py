
from django.urls import path
from E_rent import views 
from . import views

urlpatterns = [
    path("create_form/",views.create_form, name="create_form"),
    path("display_store_list/",views.display_store_list, name="display_store_list"),
    path("delete_store/<int:id>/", views.delete_store,name="delete_store"),
    
    path("update_store_info/<int:id>/",views.update_store_info, name="update_store_info"),
    
    path("salam_form/",views.salam_form,name="salam_form"),
    path("display_salam/", views.display_salam,name="display_salam"),
    path("delete_salam/<int:id>/",views.delete_salam , name="delete_salam"),
    path("update_salam_form/<int:id>/",views.update_salam_form, name="update_salam_form"),
    
    
    path("Salamoffice_form/",views.Salamoffice_form,name="Salamoffice_form"),
    path("Dis_Salamoffice_form/",views.Dis_Salamoffice_form, name="Dis_Salamoffice_form"),
    path("del_salamoffice/<int:id>/",views.del_salamoffice,name="del_salamoffice"),
    path("update_Salamoffice_form/<int:id>/",views.update_Salamoffice_form , name="update_Salamoffice_form")
]

# /E_rent/create_form/
# /E_rent/display_store_list/

