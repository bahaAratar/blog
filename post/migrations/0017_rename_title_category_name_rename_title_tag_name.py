# Generated by Django 4.2.6 on 2024-01-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_rename_name_category_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]