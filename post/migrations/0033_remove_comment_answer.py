# Generated by Django 4.2.6 on 2024-01-23 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_alter_comment_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='answer',
        ),
    ]