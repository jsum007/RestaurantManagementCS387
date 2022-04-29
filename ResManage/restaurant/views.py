from os import stat
from django.shortcuts import render
from restaurant.models import *
from django.db import connection
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status , viewsets
from rest_framework.views import APIView
from .models import *


import subprocess
import random
import string, secrets

# Create your views here.

cursor = connection.cursor()

class StaffLogin(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        #cursor.execute('select staff_id, password, role_assigned from staff where staff_id=%s;', username)
        try:
            user = Staff.objects.get(staff_id=username)
            cusid, pswd, role_ass = user.staff_id, user.password, user.role_assigned
            if pswd ==password:
                return Response({
                    'staff_id' : cusid,
                    'role_assigned': role_ass
                },
                status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Invalid Password'
                }, status= status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({
                    'message': 'Invalid User!'
                }, status= status.HTTP_401_UNAUTHORIZED)

class CustomerLogin(APIView):
    def post(self,request):
        #print('HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIi')

        if request.method == 'POST':
            #print( request.POST.get("username"))
            username = request.data['username']
            #print(username)
            password = request.data['password']

            #cursor.execute("""select customer_id, password from customer where username=%s;""", str(username))
            
      
            try:
                user = Customer.objects.get(username=username)
                cusid, pswd = user.customer_id ,user.password
                if pswd ==password:
                    return Response({
                        'customer_id' : cusid
                    },
                    status=status.HTTP_200_OK)
                else:
                    return Response({
                        'message': 'Invalid Password'
                    }, status= status.HTTP_401_UNAUTHORIZED)
            except:
                return Response({
                        'message': 'Invalid User!'
                    }, status= status.HTTP_401_UNAUTHORIZED)
        

def register_staff(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        acc_no = request.POST['acc_no']
        ifsc_code = request.POST['ifsc_code']
        role_assigned = request.POST['role_assigned']
        base_salary = request.POST['base_salary']
        last_id = cursor.execute('select max(staff_id) from staff;')
        try:
            cursor.execute('insert into staff(staff_id,name,password,attendance,acc_no,ifsc_code,role_assigned,base_salary) values (%s,%s,%s,%s,%s) RETURNING staff_id INTO new_staff_id;',last_id+1,name, password,None,acc_no,ifsc_code,role_assigned, base_salary)
            return Response({
                    'staff_id' : last_id+1,
                    'role_assigned': role_assigned
                },
                status=status.HTTP_200_OK)
        except:
            return  Response({
                    'message': 'Invalid Details!'
                }, status= status.HTTP_400_BAD_REQUEST)


def register_customer(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        name = request.POST['name']
        home_address = request.POST['home_address']
        work_address = request.POST['work_address']
        home_pincode = request.POST['home_pincode']
        work_pincode = request.POST['work_pincode']
        mail_id = request.POST['email']
        phone = request.POST['phone']
        # card_number = request.POST['card_number']
        # upi_id = request.POST['upi_id']
        # membership_status = request.POST['membership_status']
        last_id = cursor.execute('select max(customer_id) from customer;')
        try:
            cursor.execute('insert into customer(customer_id,customer_name,phone_no,home_address,work_address,mail_id,username,password,card_number,upi_id,home_pincode,work_pincode,membership_status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING customer_id INTO new_customer_id;', last_id+1, name, phone, home_address, work_address, mail_id, username, password, None, None, home_pincode, work_pincode, None)
            return Response({
                    'customer_id' : last_id+1
                },
                status=status.HTTP_200_OK)
        except:
            return  Response({
                    'message': 'Invalid Details!'
                }, status= status.HTTP_400_BAD_REQUEST)



def choose_table_id(request):
    data = json.loads(request.body)
    cursor.execute(
        'update top(1) dine_table set available = false where available=true and outlet_id=%s;', data.outlet_id)
    #rows = cursor.fetchall()
    return 


def inventory_update(request):
    data = json.loads(request.body)
    cursor.execute('update outlet_ingredient set quantity = %s where ingredient_id=%s and outlet_id=%s;',
                   data.quantity, data.ingredient_id, data.outlet_id)
    return


def place_order(request):
    data = json.loads(request.body)
    cursor.execute('insert into order_relation(outlet_id,customer_id,deli_id,payment_mode,order_type) values (%s,%s,%s,%s,%s) RETURNING order_id INTO new_order_id;',
                   data.outlet_id, data.customer_id, data.deli_id, data.payment_mode, data.order_type)
    cursor.execute('insert into order_dish (order_id,dish_id,chef_id,quantity) values (%s,%s,%s,%s);',
                   data.order_id, data.dish_id, data.chef_id, data.quantity)
    cursor.execute('with mid_quantity as (select dish_ingredient.ingredient_id as in_id,order_dish.quantity as cnt_num,dish_ingredient.quantity as base_quantity from order_dish,dish_ingredient where dish_ingredient.dish_id=order_dish.dish_id and order_dish.dish_id=%s ) update outlet_ingredient set quantity=quantity-mid_quantity.base_quantity*mid_quantity.cnt_num from mid_quantity where mid_quantity.in_id=outlet_ingredient.ingredient_id;', data.dish_id)
    return


def salary_update(request):
    # data = json.loads(request.body)
    cursor.execute('update staff set base_salary=12000 where staff_id=12;')
    cursor.execute('select * from staff where staff_id=12;')
    r = cursor.fetchall()
    print(r)

    return render(request, {'r': r})
