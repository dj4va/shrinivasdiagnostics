# Generated by Django 4.1.1 on 2022-10-22 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_component_alter_product_cutoff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantitytemperature',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
