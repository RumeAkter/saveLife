# Generated by Django 4.1.4 on 2022-12-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveline', '0011_editprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='')),
                ('des', models.TextField(max_length=200)),
            ],
        ),
    ]