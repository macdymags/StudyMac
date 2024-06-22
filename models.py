from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

'''
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    user_permissions = models.ManyToManyField(
        Permission, related_name="user_set"
    )
'''

class Shipment(models.Model):
    sender_name = models.CharField(max_length=200, default='Me')
    sender_address = models.CharField(max_length=200)
    sender_id = models.CharField(max_length=50)
    receiver_name = models.CharField(max_length=200)
    receiver_address = models.CharField(max_length=200)
    receiver_id = models.CharField(max_length=50)
    package_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    package_description = models.TextField()
    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)
    expected_delivery_date = models.DateField()

    def balance_remaining(self):
        return self.shipping_cost - self.amount_paid


class Transit(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'package_name', 'shipping_cost', 'amount_paid', 'balance_remaining', 'expected_delivery_date')


class TransitAdmin(admin.ModelAdmin):
    list_display = ('shipment', 'status', 'date_created')



