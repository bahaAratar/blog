from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aricales')

    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ManyToManyField(Category, related_name='categories', blank=True)
    tag = models.ManyToManyField(Tag, related_name='tags', blank=True)
    image = models.ManyToManyField('ArticleImage', related_name='article_images', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.owner}'


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article/', null=True, blank=True)

    def __str__(self):
        return f'{str(self.image)}     -->    {self.article}'
