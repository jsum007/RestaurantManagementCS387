from django.urls import path, re_path
from django.conf.urls import include, url
from . import views

# homepage
urlpatterns = [
    path('', views.salary_update, name='index'),
    # Register
    path("register_staff", views.StaffRegister.as_view(), name='register_staff'),
    path("register_customer", views.RegisterCustomer.as_view(), name='register_customer'),
    path("fetch_menu", views.FetchMenu.as_view(), name ="fetch_menu"),
    # Login
    path("login_staff", views.StaffLogin.as_view(), name='login_staff'),
    path("login_customer", views.CustomerLogin.as_view(), name='login_customer'),
    path("place_order", views.PlaceOrder.as_view(), name = "palce-order")
    # Logout
    #path('logout', views.logout, name='logout'),
    # welcome
   
]
