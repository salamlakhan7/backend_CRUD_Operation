
from django.conf import settings 
from django.conf.urls.static import static
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
    path("update_Salamoffice_form/<int:id>/",views.update_Salamoffice_form , name="update_Salamoffice_form"),
    
    path("form_Restaurants/",views.form_Restaurants , name="form_Restaurants"),
    path("List_Restaurants/",views.List_Restaurants , name="List_Restaurants"),
    path("delelte_resturants/<int:id>/",views.delelte_resturants, name="delelte_resturants"),
    path("update_resturants/<int:id>/", views.update_resturants, name="update_resturants"),
    
    # Authentication part  signup login logout Dashboard 
    path("signup/",views.signup_view , name="signup"),
    path("login/",views.login_view, name="login"),
    path("logout/",views.logout_view,name="logout")
]

# /E_rent/create_form/
# /E_rent/display_store_list/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
