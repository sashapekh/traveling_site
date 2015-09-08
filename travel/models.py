from django.db import models

# Create your models here.


class Products(models.Model):
    class Meta:
        db_table = 'Products'

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField()


class Customer(models.Model):
    class Meta:
        db_table = 'Customer'

    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=100)
    cust_email = models.EmailField()


class Order(models.Model):
    class Meta:
        db_table = 'Order'

    order_id = models.AutoField(primary_key=True)
    cust_id = models.OneToOneField(Customer)
    prod_id = models.OneToOneField(Products)
    order_price = models.FloatField()

