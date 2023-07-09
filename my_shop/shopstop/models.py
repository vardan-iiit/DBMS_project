from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.CharField(max_length=50,null=True)
    date_of_creation = models.CharField(max_length=50,blank=True, null=True)

    class Meta:
       db_table = 'customer'

class Product(models.Model):
    product_id = models.IntegerField(db_column='product_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    product_reviews = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'product'

class PhoneNumber(models.Model):
    phone_number = models.IntegerField(primary_key=True)
    location_pincode = models.IntegerField()

    class Meta:
        db_table = 'phone_number'

class Cart(models.Model):
    cart_id = models.IntegerField(db_column='cart_ID', primary_key=True)  # Field name made lowercase.
    cart_amount = models.FloatField(blank=True, null=True)
    cart_noitems = models.IntegerField(blank=True, null=True)
    cust = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'cart'

class InCartProducts(models.Model):
    incart_id = models.IntegerField(db_column='incart_ID', primary_key=True)  # Field name made lowercase.
    pro = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    cart = models.ForeignKey(Cart, models.DO_NOTHING, blank=True, null=True)
    quantity_of_products = models.IntegerField()

    class Meta:
        db_table = 'in_cart_products'
    
class Seller(models.Model):
    seller_id = models.IntegerField(db_column='seller_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    bank_ifsc_code = models.IntegerField(db_column='bank_IFSC_code')  # Field name made lowercase.
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'seller'

class ShippingAddress(models.Model):
    shipping_id = models.IntegerField(db_column='shipping_ID', primary_key=True)  # Field name made lowercase.
    reciever_name = models.CharField(max_length=255, blank=True, null=True)
    receiver_phonenumber = models.IntegerField(db_column='receiver_phoneNumber', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.IntegerField(blank=True, null=True)
    cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'shipping_address'

class ProductStock(models.Model):
    stock_id = models.IntegerField(db_column='stock_ID', primary_key=True)  # Field name made lowercase.
    stock_left = models.IntegerField(blank=True, null=True)
    total_stock = models.IntegerField(blank=True, null=True)
    pro = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'product_stock'

class Category(models.Model):
    category_id = models.IntegerField(db_column='category_ID', primary_key=True)  # Field name made lowercase.
    category_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'



class Orders(models.Model):
    order_id = models.IntegerField(db_column='order_ID', primary_key=True)  # Field name made lowercase.
    cart = models.ForeignKey(Cart, models.DO_NOTHING, blank=True, null=True)
    shipp = models.ForeignKey('ShippingAddress', models.DO_NOTHING, blank=True, null=True)
    order_placed_on = models.DateTimeField(blank=True, null=True)
    payable_amount = models.FloatField()
    stats = models.CharField(max_length=255)

    class Meta:
        db_table = 'orders'



class Payments(models.Model):
    transaction_id = models.IntegerField(db_column='transaction_ID', primary_key=True)  # Field name made lowercase.
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=255)
    delivery_charges = models.FloatField(blank=True, null=True)
    status_of_transaction = models.CharField(max_length=255)

    class Meta:
        db_table = 'payments'


class ProductDescriptors(models.Model):
    descriptor_id = models.IntegerField(db_column='descriptor_ID', primary_key=True)  # Field name made lowercase.
    pro = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    file_caption = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'product_descriptors'



class DatabaseAdministrator(models.Model):
    administrator_id = models.IntegerField(db_column='administrator_ID', primary_key=True)  # Field name made lowercase.
    admin_first_name = models.CharField(max_length=255)
    admin_last_name = models.CharField(max_length=255, blank=True, null=True)
    email_address = models.CharField(max_length=255, blank=True, null=True)
    admin_phone_number = models.IntegerField()
    position_of_responsiblity = models.CharField(max_length=255)

    class Meta:
        db_table = 'database_administrator'


class TrackingAndCancellation(models.Model):
    tracking_id = models.IntegerField(db_column='tracking_ID', primary_key=True)  # Field name made lowercase.
    order = models.ForeignKey(Orders, models.DO_NOTHING, blank=True, null=True)
    delivery_status = models.CharField(max_length=10)
    cancellation_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'tracking_and_cancellation'
