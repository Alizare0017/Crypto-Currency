# Generated by Django 4.1.3 on 2023-03-04 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user_pointless_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pointless',
        ),
    ]
