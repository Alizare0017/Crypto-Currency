# Generated by Django 4.1.4 on 2022-12-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_role_alter_user_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('COMMON', 'common'), ('PREMIUM', 'premium')], default='COMMON', max_length=8, null=True),
        ),
    ]
