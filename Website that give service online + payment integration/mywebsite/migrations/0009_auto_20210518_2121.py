# Generated by Django 3.1.7 on 2021-05-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0008_auto_20210518_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='price',
            field=models.IntegerField(default='5', verbose_name='5'),
        ),
    ]
