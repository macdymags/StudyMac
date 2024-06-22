from django.contrib import admin
from.models import Shipment , User, Transit, TransitAdmin

class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'package_name', 'shipping_cost', 'amount_paid', 'balance_remaining', 'expected_delivery_date')

admin.site.register(Shipment, ShipmentAdmin)
admin.site.register(User,)
admin.site.register(Transit, TransitAdmin)