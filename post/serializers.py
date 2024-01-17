from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Article
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'