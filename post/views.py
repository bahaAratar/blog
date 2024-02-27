from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
from .models import *
from .serializers import *
from .permitions import IsOwner


class ArticleListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class ArticleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwner]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [IsAdminUser]


class CategoryCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagCreateAPIView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_class = [IsAuthenticated]


class TagCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class ImageListAPIView(generics.ListAPIView):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
#
#
# class ImageCreateAPIView(generics.CreateAPIView):
#     queryset = ArticleImage.objects.all()
#     serializer_class = ArticleImageSerializer
#     permission_class = [IsAuthenticated]
#
#
# class ImageCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ArticleImage.objects.all()
#     serializer_class = ArticleImageSerializer
#     permission_classes = [IsAuthenticated]


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CommentCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner]