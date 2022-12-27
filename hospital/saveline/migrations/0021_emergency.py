# Generated by Django 4.1.4 on 2022-12-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveline', '0020_confirm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ambulance_number', models.PositiveIntegerField()),
                ('contact', models.PositiveIntegerField()),
                ('place', models.TextField()),
            ],
        ),
    ]
