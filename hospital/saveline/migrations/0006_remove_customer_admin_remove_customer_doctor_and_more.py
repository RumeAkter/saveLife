# Generated by Django 4.1.4 on 2022-12-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveline', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='patient',
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor')], max_length=200, null=True),
        ),
    ]
