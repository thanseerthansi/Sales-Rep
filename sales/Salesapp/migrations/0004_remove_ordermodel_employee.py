# Generated by Django 4.1 on 2022-08-24 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Salesapp', '0003_rename_sub_productname_subproductmodel_product_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='employee',
        ),
    ]
