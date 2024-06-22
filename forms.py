from django import forms
from .models import Shipment


class Shipment(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'

# forms.py

'''


class ShippingInfoForm(forms.Form):
    sender_name = forms.CharField(label='Sender Name')
    sender_address = forms.CharField(label='Sender Address')
    sender_id = forms.CharField(label='Sender ID Number')
    receiver_name = forms.CharField(label='Receiver Name')
    receiver_address = forms.CharField(label='Receiver Address')
    reciever_id = forms.CharField(label='Reciever ID Number')
    package_name = forms.CharField(label='Package Name')
    quantity = forms.IntegerField(label='Use intergers')
    package_description = forms.CharField(label='Package Description')
    shipping_cost = forms.DecimalField(label='Package Weight')
    shipping_cost_paid = forms.BooleanField(label='Amount Paid', required=False)
    expected_delivery_date = forms.DateField()
'''
