# Generated by Django 4.1.3 on 2022-12-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0021_gold_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=6),
        ),
    ]
