from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleImage
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all(), many=True, required=False)
    tag = serializers.SlugRelatedField(slug_field='name', queryset=Tag.objects.all(), many=True, required=False)
    comment = CommentSerializer(many=True, read_only=True)
    images = ArticleImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        required=False,
        write_only=True)

    class Meta:
        model = Article
        fields = ["id", "owner", "title", "text", "category", "tag", "comment", "images", "uploaded_images"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        article_id = representation['id']
        representation['images'] = ArticleImageSerializer(ArticleImage.objects.filter(article_id=article_id), many=True).data
        representation['comment'] = CommentSerializer(Comment.objects.filter(article_id=article_id), many=True).data
        return representation

    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        tags_data = validated_data.pop('tag')
        uploaded_images = validated_data.pop('uploaded_images')

        article = Article.objects.create(**validated_data)
        article.category.set(categories_data)
        article.tag.set(tags_data)

        for image in uploaded_images:
            ArticleImage.objects.create(article=article, image=image)

        return article
