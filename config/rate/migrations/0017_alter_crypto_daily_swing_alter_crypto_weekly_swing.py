# Generated by Django 4.1.3 on 2022-12-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0016_alter_crypto_daily_swing_alter_crypto_weekly_swing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='daily_swing',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='weekly_swing',
            field=models.FloatField(),
        ),
    ]
