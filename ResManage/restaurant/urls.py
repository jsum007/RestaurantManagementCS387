from django.urls import path, re_path
from django.conf.urls import include, url
from . import views

# homepage
urlpatterns = [
    path("register_staff", views.StaffRegister.as_view(), name='register_staff'),
    path("register_customer", views.RegisterCustomer.as_view(), name='register_customer'),
    path("fetch_menu", views.FetchMenu.as_view(), name ="fetch_menu"),
    path("login_staff", views.StaffLogin.as_view(), name='login_staff'),
    path("login_customer", views.CustomerLogin.as_view(), name='login_customer'),
    path("place_order", views.PlaceOrder.as_view(), name = "place_order"),
    path("generate_bill", views.GenerateBill.as_view(), name = "generate_bill"),
    path("order_prepared", views.OrderPrepared.as_view(), name = "order_prepared"),
    path("order_delivered", views.OrderDelivered.as_view(), name = "order_delivered"),
    path("order_preparing", views.OrderPreparing.as_view(), name = "order_preparing"),
    path("get_order_state", views.GetOrderState.as_view(), name = "get_order_state"),
    path("assign_outlet", views.AssignOutlet.as_view(), name = "assign_outlet"),
    path("add_to_cart", views.AddToCart.as_view(), name = "add_to_cart"),
    path("get_staff", views.GetStaff.as_view(), name = "get_staff"),
    path("get_chef_details", views.GetChefDetails.as_view(), name = "get_chef_details"),
    path("get_customer_details", views.GetCustomerDetails.as_view(), name = "get_customer_details"),
    path("get_waiter_details", views.GetWaiterDetails.as_view(), name = "get_waiter_details"),
    path("available_table", views.AvailableTable.as_view(), name = "available_table"),
    path("choose_table", views.ChooseTable.as_view(), name = "choose_table"),
    path("inventory_update", views.InventoryUpdate.as_view(), name = "inventory_update"),
    path("get_dishes_to_prepare", views.GetDishesToPrepare.as_view(), name = "get_dishes_to_prepare")
    ]
