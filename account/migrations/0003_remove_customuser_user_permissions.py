# Generated by Django 4.2.6 on 2023-10-28 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_customuser_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
    ]
