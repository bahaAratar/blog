# Generated by Django 4.2.6 on 2024-01-19 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_article_category_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='post.category'),
            preserve_default=False,
        ),
    ]
