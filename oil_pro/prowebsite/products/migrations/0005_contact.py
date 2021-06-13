# Generated by Django 3.1.1 on 2021-06-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_subject', models.CharField(max_length=50)),
                ('contact_message', models.CharField(max_length=400)),
            ],
        ),
    ]
