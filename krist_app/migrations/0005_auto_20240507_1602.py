# Generated by Django 3.0.5 on 2024-05-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krist_app', '0004_auto_20240507_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_moblieno',
            field=models.IntegerField(max_length=10),
        ),
    ]