# Generated by Django 3.1.7 on 2021-05-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0009_auto_20210518_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.IntegerField(default='5', verbose_name='price'),
        ),
    ]