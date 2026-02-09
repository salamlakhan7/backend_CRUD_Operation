from django import urls
from django.urls import path
from E_shop import views
from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
from E_rent import views 
from . import views

urlpatterns = [
    
    path("",views.land_page,name="land_page"),
    
    path("create_shop/",views.create_shop,name="create_shop"),
    path("shop_list/",  views.shop_list,  name="shop_list"),
    
    path("signup/",views.signup_view,name="signup_view"),
    path("login/",views.login_view,name="login_view"),
    path("logout/",views.logout_view,name="logout_view"),
    
    path("delete_shop/<int:id>/",views.delete_shop,name="delete_shop"),
    path("update_shop/<int:id>/",views.update_shop,name="update_shop")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)