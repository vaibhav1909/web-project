# Generated by Django 3.1.1 on 2021-06-12 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20210612_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='custmer_photo',
            new_name='customer_photo',
        ),
    ]
