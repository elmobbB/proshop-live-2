# Generated by Django 5.0.6 on 2024-08-25 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_devliveredat_order_deliveredat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='/placeholder.jpeg', null=True, upload_to=''),
        ),
    ]
