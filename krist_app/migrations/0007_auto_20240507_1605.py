# Generated by Django 3.0.5 on 2024-05-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krist_app', '0006_auto_20240507_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_moblieno',
            field=models.CharField(max_length=50),
        ),
    ]