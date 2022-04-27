from django.shortcuts import render
from restaurant.models import *
from django.db import connection
import json

# Create your views here.

cursor = connection.cursor()

def choose_table_id(request):
    data = json.loads(request.body)
    cursor.execute('update top(1) dine_table set available = false where available=true and outlet_id=%s;', data.outlet_id)
    #rows = cursor.fetchall()
    return

def inventory_update(request):
    data = json.loads(request.body)
    cursor.execute('update outlet_ingredient set quantity = %s where ingredient_id=%s and outlet_id=%s;', data.quantity, data.ingredient_id, data.outlet_id)
    return

def place_order(request):
    data = json.loads(request.body)
    cursor.execute('insert into order_relation(outlet_id,customer_id,deli_id,payment_mode,order_type) values (%s,%s,%s,%s,%s) RETURNING order_id INTO new_order_id;', data.outlet_id, data.customer_id, data.deli_id, data.payment_mode, data.order_type)
    cursor.execute('insert into order_dish (order_id,dish_id,chef_id,quantity) values (%s,%s,%s,%s);', data.order_id, data.dish_id, data.chef_id, data.quantity)
    cursor.execute('with mid_quantity as (select dish_ingredient.ingredient_id as in_id,order_dish.quantity as cnt_num,dish_ingredient.quantity as base_quantity from order_dish,dish_ingredient where dish_ingredient.dish_id=order_dish.dish_id and order_dish.dish_id=%s ) update outlet_ingredient set quantity=quantity-mid_quantity.base_quantity*mid_quantity.cnt_num from mid_quantity where mid_quantity.in_id=outlet_ingredient.ingredient_id;', data.dish_id)
    return

def salary_update(request):
    data = json.loads(request.body)
    cursor.execute('update staff set base_salary=%s where staff_id=%s;', data.salary, data.chef_id)
    return
