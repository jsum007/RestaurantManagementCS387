from django.urls import path, re_path
from django.conf.urls import include, url
from . import views

# homepage
urlpatterns = [
    path('', views.salary_update, name='index'),
    # Register
    path("register_staff", views.register_staff, name='register_staff'),
    path("register_customer", views.register_customer, name='register_customer'),
    # Login
    path("login_staff", views.StaffLogin.as_view(), name='login_staff'),
    path("login_customer", views.CustomerLogin.as_view(), name='login_customer'),
    # Logout
    #path('logout', views.logout, name='logout'),
    # welcome
   
]
