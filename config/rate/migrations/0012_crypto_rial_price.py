# Generated by Django 4.1.3 on 2022-12-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0011_crypto'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='rial_price',
            field=models.IntegerField(null=True),
        ),
    ]
