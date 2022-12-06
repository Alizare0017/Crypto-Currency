# Generated by Django 4.1.3 on 2022-12-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='country',
        ),
        migrations.AddField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='high',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='low',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='rate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
