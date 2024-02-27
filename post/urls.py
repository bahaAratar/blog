from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListAPIView.as_view()),
    path('create/', ArticleListCreateAPIView.as_view()),
    path('crud/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view()),

    path('category/', CategoryListAPIView.as_view()),
    path('category/create/', CategoryCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryCRUDAPIView.as_view()),

    path('tag/', TagListAPIView.as_view()),
    path('tag/create/', TagCreateAPIView.as_view()),
    path('tag/<int:pk>/', TagCRUDAPIView.as_view()),

    path('image/', ImageListAPIView.as_view()),

    path('comment/', CommentListAPIView.as_view()),
    path('comment/create/', CommentCreateAPIView.as_view()),
    path('comment/<int:pk>/', CommentCRUDAPIView.as_view())
]

