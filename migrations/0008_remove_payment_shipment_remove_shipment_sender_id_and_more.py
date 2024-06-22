# Generated by Django 4.2.7 on 2024-03-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracApp', '0007_remove_shipment_address_remove_shipment_amount_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='shipment',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='Sender_id',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='is_shipping_cost_paid',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='reciever_address',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='reciever_id',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='reciever_name',
        ),
        migrations.RemoveField(
            model_name='shipment',
            name='sender_name',
        ),
        migrations.AddField(
            model_name='shipment',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='shipment',
            name='receiver_address',
            field=models.CharField(default='hhhh', max_length=200),
        ),
        migrations.AddField(
            model_name='shipment',
            name='receiver_id',
            field=models.CharField(default='hhhh', max_length=50),
        ),
        migrations.AddField(
            model_name='shipment',
            name='receiver_name',
            field=models.CharField(default='hhhh', max_length=200),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='package_description',
            field=models.TextField(default='hhhh'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='package_name',
            field=models.CharField(default='hhhh', max_length=200),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='quantity',
            field=models.PositiveIntegerField(default='hhhh'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='sender_address',
            field=models.CharField(default='hhhh', max_length=200),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AddField(
            model_name='shipment',
            name='sender_id',
            field=models.CharField(default='hhhh', max_length=50),
        ),
    ]