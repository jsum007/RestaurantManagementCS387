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
active_order_tblwise = {}
tblwise_dish_list = {}
outletwise_active_ords ={}



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
    def get(self, request):
        cursor.execute('select dish_id, dish_name, price, cuisine_name from dish, cuisine where dish.cuisine_id = cuisine.cuisine_id')
        rows = cursor.fetchall()
        dishes = []
        for r in rows:
            cursor.execute('select name, veg, exotic from ingredients, dish_ingredient, dish where dish.dish_id = dish_ingredient.dish_id and dish_ingredient.ingredient_id = ingredients.ingredient_id and dish.dish_id = %s', (r[0],))
            ing = cursor.fetchall()
            ings = []
            isveg =1
            for i in ing:
                if i[2] == 1:
                    ings.append(i[0])
                if i[1] == 0:
                    isveg = 0
            dishes.append((r[0], r[1], r[2], r[3], tuple(ings), isveg))
        rs = json.dumps(dishes)
        return HttpResponse(rs, content_type='application/json')




class PlaceOrder(APIView):
    def post(self, request):
        dishes_ = request.data['dishes']
        quan_ = request.data['quantity']
        cusid = request.data['customer_id']
        tbid = request.data['table_id'] #'-1' if delivery
        outid = request.data['outlet_id']
                

    
        ##Idea is to add all the dishes to pending dishes, assign new order id, use table id to get waiter id , add order id to pending orders
        ## When Generate Billis clicked fetch payment mode,
        try: 
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
                tblwise_dish_list[(outid,tbid)] = dishes_
                active_order_tblwise[(outid,tbid)] = new_order_id
                #print(del_id)
            else:
                waiter_id = -1
            cursor.execute('select staff_id from delivery_person where outlet_id = %s', (outid,))
            rows_1 = cursor.fetchall()
            del_ppl =[]
            for r in rows_1:
                del_ppl.append(r[0])
            del_id = random.choice(del_ppl)

            for di in range(len(dishes_)):
                cursor.execute('select ingredient_id, quantity from dish_ingredient where dish_id = %s', (dishes_[di],))
                rows = cursor.fetchall()
                ing_id = []
                ing_quan = []
                for r in rows:
                    ing_id.append(r[0])
                    ing_quan.append(r[1]*quan_[di])
            
            for i in range(len(ing_id)):
                cursor.execute('update outlet_ingredient set quantity = quantity - %s where ingredient_id = %s and outlet_id = %s', (ing_quan[i], ing_id[i], outid))
                


            pending_order_list[new_order_id] = [dishes_, quan_, cusid, tbid, outid, del_id,waiter_id]
            for di in range(len(dishes_)):
                dish_states[(new_order_id, dishes_[di])]=0
                dish_quantity[(new_order_id, dishes_[di])]=quan_[di]
            #print(pending_order_list)
            #print(dish_states)
            if outid in  outletwise_active_ords.keys():
                outletwise_active_ords[outid].append(new_order_id)
            else:
                outletwise_active_ords[outid] = [new_order_id]
            # print(active_order_tblwise)
            # print(dish_states)
            print(pending_order_list)
            # print(outletwise_active_ords)
            return Response({
                'order_id' : new_order_id
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message' : 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)
        

class GenerateBill(APIView):
    def post(self, request):
        ordid = request.data['order_id']
        paymode = request.data['paymode']
        
        dishes_, quan_, cusid, tbid, outid, del_id, waiter_id = pending_order_list[ordid]
        
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
            flag =0            
            for key, value in dish_states.items():
                ordid_ , _ = key
                if ordid_ == ordid and value !=2:
                    flag =1
                    break

            if flag == 0:
                cursor.execute('select outlet_id from chef where staff_id = %s', (chef_id,))
                outid = cursor.fetchone()[0]
                outletwise_active_ords[outid].remove(ordid)

                for key, value in active_order_tblwise.items():
                    if value == ordid:
                        outid, tbid = key
                        cursor.execute('update dine_table set available =%s where table_id = %s and outlet_id = %s', (1, tbid, outid))
                        active_order_tblwise.pop(key)
                        break
                
                pending_order_list.pop(ordid)

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
        
   

class AddToCart(APIView):
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
        if True:
            cursor.execute('select staff.staff_id , staff.name, staff.attendance, staff.acc_no, staff.ifsc_code, staff.role_assigned, staff.base_salary from staff, chef where staff.staff_id = chef.staff_id and outlet_id = %s', (outlet_id, ))
            rows1 = cursor.fetchall()
            cursor.execute('select staff.staff_id , staff.name, staff.attendance, staff.acc_no, staff.ifsc_code, staff.role_assigned, staff.base_salary from staff, manager where staff.staff_id = manager.staff_id and outlet_id = %s', (outlet_id, ))
            rows2 = cursor.fetchall()
            cursor.execute('select staff.staff_id , staff.name, staff.attendance, staff.acc_no, staff.ifsc_code, staff.role_assigned, staff.base_salary from staff, other_staff where staff.staff_id = other_staff.staff_id and outlet_id = %s', (outlet_id, ))
            rows3 = cursor.fetchall()
            cursor.execute('select staff.staff_id , staff.name, staff.attendance, staff.acc_no, staff.ifsc_code, staff.role_assigned, staff.base_salary from staff, delivery_person where staff.staff_id = delivery_person.staff_id and outlet_id = %s', (outlet_id, ))
            rows4 = cursor.fetchall()
            cursor.execute('select staff.staff_id , staff.name, staff.attendance, staff.acc_no, staff.ifsc_code, staff.role_assigned, staff.base_salary from staff, waiter where staff.staff_id = waiter.staff_id and outlet_id = %s', (outlet_id, ))
            rows5 = cursor.fetchall()

            staff_ids1 = []
            staff_ids2 = []
            staff_ids3 = []
            staff_ids4 = []
            staff_ids5 = []
            for r in rows1:
                staff_ids1.append((r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
            for r in rows2:
                staff_ids2.append((r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
            for r in rows3:
                staff_ids3.append((r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
            for r in rows4:
                staff_ids4.append((r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
            for r in rows5:
                staff_ids5.append((r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

            return Response({
                'chef' : staff_ids1,
                'manager' : staff_ids2,
                'other_staff' : staff_ids3,
                'delivery_person' : staff_ids4,
                'waiter' : staff_ids5
            }, status=status.HTTP_200_OK)
        # except:
        #     return Response({
        #         'message': 'Invalid Details!'
        #     }, status=status.HTTP_400_BAD_REQUEST)
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


class AvailableTable(APIView):
    def post(self, request):
        outid = request.data['outlet_id']
        try:
            cursor.execute('select table_id from dine_table where outlet_id = %s and available = 1', (outid, ))
            rows = cursor.fetchall()
            table_ids = []
            for r in rows:
                table_ids.append(r[0])
            return Response({
                'available_tables' : table_ids
            }, status=status.HTTP_200_OK)
        except: 
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class ChooseTable(APIView):
    def post(self, request):
        table_id = request.data['table_id']
        outid = request.data['outlet_id']
        #status = request.data['status']
        try:
            cursor.execute('update dine_table set available =0 where table_id = %s and outlet_id = %s', (table_id, outid))
            return Response({
                'message' : 'Table Status Changed!'
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class InventoryUpdate(APIView):
    def post(self, request):
        outid = request.data['outlet_id']
        item_id = request.data['ingredient_id']
        quantity = request.data['quantity']
        try:
            cursor.execute('update outlet_ingredient set quantity = quantity + %s where ingredient_id = %s and outlet_id = %s', (quantity, item_id, outid))
            return Response({
                'message' : 'Item Quantity Updated!'
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST)

class GetDishesToPrepare(APIView):
    def post(self, request):
        outid = request.data['outlet_id']
        chefid = request.data['chef_id']
        try:
            cursor.execute('select cuisine_id from chef_expertise where staff_id = %s', (chefid, ))
            expert = cursor.fetchone()[0]
            active_ords = outletwise_active_ords[outid]
            dish_ids = []
            quants =[]
            for ord in active_ords:
                dishes_, quan_, cusid, tbid,_, del_id, waiter_id = pending_order_list[ord]
                for i in range(len(dishes_)):
                    if dish_states[(ord, dishes_[i])] ==0:
                        cursor.execute('select cuisine_id from dish where dish_id = %s', (dishes_[i], ))
                        dish_cuisine = cursor.fetchone()[0]
                        if dish_cuisine == expert:
                            dish_ids.append(dishes_[i])
                            quants.append(quan_[i])
            
            return Response({
                'dishes' : dish_ids,
                'quantities' : quants
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                'message': 'Invalid Details!'
            }, status=status.HTTP_400_BAD_REQUEST) 

            


def salary_update(request):
    # data = json.loads(request.body)
    cursor.execute('update staff set base_salary=12000 where staff_id=12;')
    cursor.execute('select * from staff where staff_id=12;')
    r = cursor.fetchall()
    print(r)

    return render(request, {'r': r})
