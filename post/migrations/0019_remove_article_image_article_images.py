# Generated by Django 4.2.6 on 2024-01-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_articleimage_remove_article_image_delete_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='articles', to='post.articleimage'),
        ),
    ]
