# Generated by Django 4.1 on 2022-08-26 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Salesapp', '0008_remove_ordermodel_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproductmodel',
            name='subproduct_id',
            field=models.IntegerField(null=True),
        ),
    ]
