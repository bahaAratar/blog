from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aricales')

    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ManyToManyField(Category, related_name='categories', blank=True)
    tag = models.ManyToManyField(Tag, related_name='tags', blank=True)
    # image = models.ImageField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.owner}'
