# Generated by Django 3.0.5 on 2024-05-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krist_app', '0005_auto_20240507_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_moblieno',
            field=models.IntegerField(),
        ),
    ]
