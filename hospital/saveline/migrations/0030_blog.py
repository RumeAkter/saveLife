# Generated by Django 4.1.4 on 2022-12-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saveline', '0029_alter_payment_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog')),
                ('pic', models.ImageField(upload_to='blogpic')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]