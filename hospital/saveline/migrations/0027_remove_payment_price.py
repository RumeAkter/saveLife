# Generated by Django 4.1.4 on 2022-12-23 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saveline', '0026_blood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='price',
        ),
    ]
