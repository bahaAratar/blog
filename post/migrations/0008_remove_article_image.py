# Generated by Django 4.2.6 on 2024-01-19 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_remove_article_tag_article_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
