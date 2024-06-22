# Generated by Django 4.2.7 on 2024-02-26 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PracApp', '0004_rename_shipping_info_item_shipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='shipment',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
