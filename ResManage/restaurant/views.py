from os import stat
from django.shortcuts import render
from requests import request
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
from itertools import groupby
from collections import defaultdict
import random

pending_order_list ={}
dish_states = {}
dish_quantity = {}



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
        

class StaffRegister(APIView):
    def post(self,request):
        name = request.data['name']
        password = request.data['password']
        acc_no = request.data['acc_no']
        ifsc_code = request.data['ifsc_code']
        role_assigned = request.data['role_assigned']
        base_salary = int(request.data['base_salary'])
        cursor.execute('select max(staff_id) from staff;')
        last_id = cursor.fetchone()[0]
        #print(last_id)
        try:
            assert len(password)>=8
            Staff.objects.create(staff_id=last_id+1, name=name, password=password, attendance=0, acc_no = acc_no,ifsc_code = ifsc_code, role_assigned = role_assigned, base_salary=base_salary)  

            #cursor.execute('insert into staff(staff_id,name,password,attendance,acc_no,ifsc_code,role_assigned,base_salary) values (%s,%s,%s,%s,%s) RETURNING staff_id INTO new_staff_id;',last_id+1,name, password,None,acc_no,ifsc_code,role_assigned, base_salary)
            return Response({
                    'staff_id' : last_id+1,
                    'role_assigned': role_assigned
                },
                status=status.HTTP_200_OK)
        except:
            return  Response({
                    'message': 'Invalid Details!'
                }, status= status.HTTP_400_BAD_REQUEST)


class RegisterCustomer(APIView):
    def post(self, request):
        username = request.data['username'] 
        password = request.data['password']
        name = request.data['name']
        home_address = request.data['home_address']
        work_address = request.data['work_address']
        home_pincode = request.data['home_pincode']
        work_pincode = request.data['work_pincode']
        mail_id = request.data['email']
        phone = request.data['phone']
        # card_number = request.data['card_number']
        # upi_id = request.data['upi_id']
        # membership_status = request.data['membership_status']
        cursor.execute('select max(customer_id) from customer;')
        last_id = cursor.fetchone()[0]
        try:
            assert len(password)>=8
            assert len(work_pincode)==6
            assert len(home_pincode)==6
            cursor.execute('insert into customer(customer_id,customer_name,phone_no,home_address,work_address,mail_id,username,password,card_number,upi_id,home_pincode,work_pincode,membership_status) values (%s,%s,%s,%s,%s,%s, %s, %s, %s,%s,%s,%s,%s);', (last_id+1, name, phone, home_address, work_address, mail_id, username, password, None, None, home_pincode, work_pincode, None))

            #Customer.objects.create()
            return Response({
                    'customer_id' : last_id+1
                },
                status=status.HTTP_200_OK)
        except:
            return  Response({
                    'message': 'Invalid Details!'
                }, status= status.HTTP_400_BAD_REQUEST)

class FetchMenu(APIView):
    def get(self,request):
        #data = request.data
        cursor.execute(
            'with A as (select dish_id, dish_name, cuisine_name, price from dish, cuisine where dish.cuisine_id = cuisine.cuisine_id),B as (select dish.dish_id, name from ingredients, dish_ingredient, dish where dish.dish_id = dish_ingredient.dish_id and dish_ingredient.ingredient_id = ingredients.ingredient_id and exotic = 1) select A.dish_id, dish_name, price, cuisine_name, name from A,B where A.dish_id = B.dish_id')
        rows = cursor.fetchall()
        mergeddict = defaultdict(list)
        for group in rows:
            #print(group)
            mergeddict[group[:-1]].append(group[-1])
        f_rows = [(k + (tuple(v),))
                for k, v in mergeddict.items()]

        cursor.execute(
            'select dish_id, veg from dish_ingredient, ingredients where dish_ingredient.ingredient_id = ingredients.ingredient_id')
        rows2 = cursor.fetchall()
        #print(rows2)
        mergeddict2 = defaultdict(list)
        for group in rows2:
            mergeddict[group[:-1]].append(group[-1])
        f_rows2 = [(k + (tuple(v),) )
                for k, v in mergeddict.items()]
        f_rows3 = []
        for r in f_rows2:
            is_veg = 1
            for x in r[1]:
                if(x == 0):
                    is_veg = 0
            f_rows3.append((r[0], is_veg))
        #print(f_rows3)
        for i in range(len(f_rows)):
            f_rows[i] += (f_rows3[i][1],)
        #print(f_rows)
        rs = json.dumps(f_rows)
        return HttpResponse(rs, content_type='application/json')

class PlaceOrder(APIView):
    def post(self, request):
        dishes_ = request.data['dishes']
        quan_ = request.data['quantity']
        cusid = request.data['customer_id']
        tbid = request.data['table_id'] #'-1' if delivery
        outid = request.data['outlet_id']
        try:          

        
            ##Idea is to add all the dishes to pending dishes, assign new order id, use table id to get waiter id , add order id to pending orders
            ## When Generate Billis clicked fetch payment mode, 
            cursor.execute('SELECT MAX(order_id) FROM order_relation;')
            last_id = cursor.fetchone()[0]
            if pending_order_list.keys():
                tmp1=max(pending_order_list.keys())
            else:
                tmp1=-1
            new_order_id = max(tmp1, last_id) +1
            if int(tbid) >=0:
                cursor.execute('select staff_id from waiter_table where table_id = %s', (tbid,))
                rows_1 = cursor.fetchall()
                set1 = set()
                for d in rows_1:
                    set1.add(d[0])
                cursor.execute('select staff_id from waiter where outlet_id = %s', (outid,))
                rows_2 = cursor.fetchall()
                set2 = set()
                for d in rows_2:
                    set2.add(d[0])
                waiter_id = list(set1.intersection(set2))[0]
                del_id = -1
                #print(del_id)
            else:
                waiter_id = -1
            cursor.execute('select staff_id from delivery_person where outlet_id = %s', (outid,))
            rows_1 = cursor.fetchall()
            del_ppl =[]
            for r in rows_1:
                del_ppl.append(r[0])
            del_id = random.choice(del_ppl)


            pending_order_list[new_order_id] = [dishes_, quan_, cusid, tbid, outid, del_id,waiter_id]
            for di in range(len(dishes_)):
                dish_states[(new_order_id, dishes_[di])]=0
                dish_quantity[(new_order_id, dishes_[di])]=quan_[di]
            #print(pending_order_list)
            #print(dish_states)
            return Response({
                'order_id' : new_order_id
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class GenerateBill(APIView):
    def post(self, request):
        ordid = request.data['order_id']
        paymode = request.data['paymode']
        
        dishes_, quan_, cusid, tbid, outid, del_id, waiter_id = pending_order_list[ordid]
        pending_order_list.pop(ordid)
        try:
            ord_type = 'delivery' if int(tbid) == -1 else 'dinein'
            OrderRelation.objects.create(order_id = ordid, payment_mode = paymode, outlet_id = outid, customer_id = cusid, order_type=ord_type, staff_id = del_id)
            return Response({ 'message' : 'Bill Generated'}, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class OrderPrepared(APIView):
    def post(self, request):
        ordid = request.data['order_id']
        dish_id = request.data['dish_id']
        chef_id = request.data['chef_id']
        try:
            quant = dish_quantity[(ordid, dish_id)]
            OrderDish.objects.create(order_id = ordid, dish_id = dish_id, staff_id = chef_id, quantity=quant)
            dish_states[(ordid, dish_id)] = 2 #2 means prepared
            dish_quantity.pop((ordid, dish_id))
            return Response({'message': 'Order Prepared!'}, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class OrderPreparing(APIView):
    def post(self, request):
        ordid = request.data['order_id']
        dish_id = request.data['dish_id']
        chef_id = request.data['chef_id']
        try:
            dish_states[(ordid, dish_id)] = 1 #1 means preparing
            return Response({'message': 'Order Preparing!'}, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class OrderDelivered(APIView):
    def post(self, request):
        ordid = request.data['order_id']
        dish_id = request.data['dish_id']
        try:
            dish_states[(ordid, dish_id)] = 3 #3 means delivered
            dish_states.pop((ordid, dish_id))
            return Response({'message': 'Order Delivered!'}, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class GetOrderState(APIView):
    def post(self, request):
        ordid = request.data['order_id']
        dish_id = request.data['dish_id']
        try:
            return Response({
                'state' : dish_states[(ordid, dish_id)]
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)


class AssignOutlet(APIView):
    def post(self, request):
        cusid = request.data['customer_id']
        isdelivery = request.data['is_delivery'] # 1 or 0
        pincode = request.data['pincode']
        try:
            if int(isdelivery) ==0:
                    cursor.execute('select home_pincode from customer where customer_id = %s', (cusid, ))
                    pincode = cursor.fetchone()[0]

            cursor.execute('select outlet_id, pin_code from outlet;')
            rows = cursor.fetchall()
            outlets_pin_dict = {}
            for r in rows:
                outlets_pin_dict[r[1]]= r[0]
            nearest_pin = 0
            dist_ = 70000000
            for p in outlets_pin_dict.keys():
                tmp_dist = abs(p-pincode)
                if tmp_dist < dist_:
                    nearest_pin = p
                    dist_ = abs(p-pincode)
            outid =outlets_pin_dict[nearest_pin]
            return Response({
                'outlet_id' : outid
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)
        
   

class AddtoCart(APIView):
    def post(self,request):
        dish_id = request.data['dish_id']
        quantity = request.data['quantity']
        outlet_id = request.data['outlet_id']
        try:
            cursor.execute('select ingredient_id, quantity from dish_ingredient where dish_id = %s', (dish_id, ))
            rows = cursor.fetchall()
            for r in rows:
                cursor.execute('select quantity from outlet_ingredient where ingredient_id = %s and outlet_id = %s', (r[0], outlet_id))
                stock = cursor.fetchone()[0]
                if stock < r[1]*quantity:
                    return Response({
                        'message': 'Not Enough Stock!'
                    }, status=status.HTTP_400_BAD_REQUEST)
            return Response({
                'message': 'Added to Cart!'
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class GetStaff(APIView):
    def post(self, request):
        outlet_id = request.data['outlet_id']
        try:
            cursor.execute('select staff_id from staff where outlet_id = %s', (outlet_id, ))
            rows = cursor.fetchall()
            staff_ids = []
            for r in rows:
                staff_ids.append((r[0], r[1], r[3], r[4], r[5], r[6], r[7]))
            return Response({
                'staff_info' : staff_ids
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)
class GetChefDetails(APIView):
    def post(self, request):
        staff_id = request.data['staff_id']
        try:
            cursor.execute('select * from staff where staff_id = %s', (staff_id, ))
            rows1 = cursor.fetchone()
            cursor.execute('select * from chef where staff_id = %s', (staff_id, ))
            rows2 = cursor.fetchone()
            cursor.execute('select cuisine_name from chef_expertise, cuisine where staff_id = %s and chef_expertise.cuisine_id = cuisine.cuisine_id', (staff_id, ))
            expert= cursor.fetchone()[0]
            return Response({
                'staff_id' : rows1[0],
                'name' : rows1[1],
                'attendance' : rows1[3],
                'account_no' : rows1[4],
                'ifsc_code' : rows1[5],
                'base_salary' : rows1[7],
                'rating' : rows2[2],
                'expertise' : expert
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class GetCustomerDetails(APIView):
    def post(self, request):
        cusid = request.data['customer_id']
        try:
            cursor.execute('select * from customer where customer_id = %s', (cusid, ))
            rows = cursor.fetchone()
            cursor.execute('select order_id from order_relation where customer_id = %s', (cusid, ))
            rows1 = cursor.fetchall()
            order_ids = []
            for r in rows1:
                order_ids.append(r[0])
            return Response({
                'customer_id' : rows[0],
                'customer_name' : rows[1],
                'phone_no' : rows[2],
                'home_address' : rows[3],
                'work_address' : rows[4],
                'email_id' : rows[5],
                'username' : rows[6],
                'card_no' : rows[8],
                'upi_id' : rows[9],
                'home_pincode' : rows[10],
                'work_pincode' : rows[11],
                'membership_status' : rows[12],
                'order_history' : order_ids
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)


class GetWaiterDetails(APIView):
    def post(self, request):
        staff_id = request.data['staff_id']
        try:
            cursor.execute('select * from staff where staff_id = %s', (staff_id, ))
            rows1 = cursor.fetchone()
            cursor.execute('select outlet_id from waiter where staff_id = %s', (staff_id, ))
            outid = cursor.fetchone()[0]
            cursor.execute('select table_id from waiter_table where staff_id = %s', (staff_id, ))
            rows2 = cursor.fetchall()
            table_ids = []
            for r in rows2:
                table_ids.append(r[0])
            return Response({
                'staff_id' : rows1[0],
                'name' : rows1[1],
                'attendance' : rows1[3],
                'account_no' : rows1[4],
                'ifsc_code' : rows1[5],
                'base_salary' : rows1[7],
                'outlet_id' : outid,
                'assigned_tables' : table_ids
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)






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
