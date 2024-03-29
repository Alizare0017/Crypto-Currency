# Generated by Django 4.1.3 on 2022-12-06 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_alter_currency_high_alter_currency_low_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='requested_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 6, 20, 53, 39, 437355)),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='currency',
            name='high',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='currency',
            name='low',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='currency',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='currency',
            name='rate',
            field=models.CharField(max_length=20),
        ),
    ]
