# Generated by Django 4.2.6 on 2024-01-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_remove_article_category_remove_article_tag_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
