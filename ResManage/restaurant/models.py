# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chef(models.Model):
    staff = models.OneToOneField('Staff', models.CASCADE, primary_key=True)
    outlet = models.ForeignKey('Outlet', models.CASCADE, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:

        db_table = 'chef'


class ChefExpertise(models.Model):
    staff = models.OneToOneField(Chef, models.CASCADE, primary_key=True)
    cuisine = models.ForeignKey('Cuisine', models.CASCADE)

    class Meta:

        db_table = 'chef_expertise'
        unique_together = (('staff', 'cuisine'),)


class Cuisine(models.Model):
    cuisine_id = models.IntegerField(primary_key=True)
    cuisine_name = models.TextField()

    class Meta:

        db_table = 'cuisine'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    phone_no = models.BigIntegerField(blank=True, null=True)
    home_address = models.TextField()
    work_address = models.TextField()
    mail_id = models.TextField()
    username = models.TextField(unique=True)
    password = models.TextField()
    card_number = models.BigIntegerField(blank=True, null=True)
    upi_id = models.TextField(blank=True, null=True)
    home_pincode = models.IntegerField()
    work_pincode = models.IntegerField()
    membership_status = models.TextField(blank=True, null=True)

    

    class Meta:

        db_table = 'customer'


class CustomerOutlet(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)
    outlet = models.OneToOneField('Outlet', models.CASCADE, primary_key=True)
    rating = models.FloatField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'customer_outlet'
        unique_together = (('outlet', 'customer'),)


class DeliveryPerson(models.Model):
    staff = models.OneToOneField('Staff', models.CASCADE, primary_key=True)
    outlet_id = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:

        db_table = 'delivery_person'


class DineTable(models.Model):
    table_id = models.IntegerField(primary_key=True)
    outlet_id = models.IntegerField()
    category = models.TextField()
    num_persons = models.IntegerField(blank=True, null=True)
    available = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'dine_table'
        unique_together = (('table_id', 'outlet_id'),)


class Dish(models.Model):
    dish_id = models.IntegerField(primary_key=True)
    dish_name = models.TextField()
    cuisine = models.ForeignKey(Cuisine, models.CASCADE, blank=True, null=True)
    category = models.TextField()
    price = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'dish'


class DishIngredient(models.Model):
    dish = models.OneToOneField(Dish, models.CASCADE, primary_key=True)
    ingredient = models.ForeignKey('Ingredients', models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    quantity_unit = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'dish_ingredient'
        unique_together = (('dish', 'ingredient'),)


class Ingredients(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    veg = models.IntegerField(blank=True, null=True)
    exotic = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'ingredients'


class Manager(models.Model):
    staff = models.OneToOneField('Staff', models.CASCADE, primary_key=True)
    outlet = models.ForeignKey('Outlet', models.CASCADE, blank=True, null=True)

    class Meta:

        db_table = 'manager'


class OrderDish(models.Model):
    order = models.OneToOneField(
        'OrderRelation', models.CASCADE, primary_key=True)
    dish = models.ForeignKey(Dish, models.CASCADE)
    staff = models.ForeignKey(Chef, models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'order_dish'
        unique_together = (('order', 'dish'),)


class OrderRelation(models.Model):
    order_id = models.AutoField(primary_key=True)
    outlet = models.ForeignKey('Outlet', models.CASCADE, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    staff = models.ForeignKey(
        DeliveryPerson, models.CASCADE, blank=True, null=True)
    payment_mode = models.TextField(blank=True, null=True)
    order_type = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'order_relation'


class OtherStaff(models.Model):
    staff = models.OneToOneField('Staff', models.CASCADE, primary_key=True)
    outlet = models.ForeignKey('Outlet', models.CASCADE, blank=True, null=True)

    class Meta:

        db_table = 'other_staff'


class Outlet(models.Model):
    outlet_id = models.IntegerField(primary_key=True)
    pin_code = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    address = models.TextField()

    class Meta:

        db_table = 'outlet'


class OutletIngredient(models.Model):
    outlet = models.OneToOneField(Outlet, models.CASCADE, primary_key=True)
    ingredient = models.ForeignKey(Ingredients, models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    quantity_unit = models.TextField(blank=True, null=True)

    class Meta:

        db_table = 'outlet_ingredient'
        unique_together = (('outlet', 'ingredient'),)


class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    password = models.TextField()
    attendance = models.IntegerField(blank=True, null=True)
    acc_no = models.BigIntegerField(blank=True, null=True)
    ifsc_code = models.TextField()
    role_assigned = models.TextField(blank=True, null=True)
    base_salary = models.IntegerField(blank=True, null=True)



    class Meta:

        db_table = 'staff'


class Waiter(models.Model):
    staff = models.OneToOneField(Staff, models.CASCADE, primary_key=True)
    outlet = models.ForeignKey(Outlet, models.CASCADE, blank=True, null=True)

    class Meta:

        db_table = 'waiter'


class WaiterTable(models.Model):
    staff = models.OneToOneField(Staff, models.CASCADE, primary_key=True)
    table = models.ForeignKey(DineTable, models.CASCADE)
    outlet_id = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'waiter_table'
        unique_together = (('staff', 'table'),)
