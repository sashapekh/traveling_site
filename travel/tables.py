__author__ = 'sashapekh'

import django_tables2 as tables
from .models import Products,Customer,Order


class ProductTable(tables.Table):
    class Meta:
        model = Products
        attrs = {'class': 'paleblue'}


class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        attrs = {'class': 'paleblue'}


class OrderTable(tables.Table):
    class Meta:
        model = Order
        attr = {'class': 'paleblue'}

