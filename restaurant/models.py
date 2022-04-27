# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:

        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.CASCADE)

    class Meta:

        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:

        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:

        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.CASCADE)

    class Meta:

        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.CASCADE)

    class Meta:

        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

    class Meta:

        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:

        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:

        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:

        db_table = 'django_session'


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
