# Generated by Django 3.0.5 on 2024-05-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krist_app', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]