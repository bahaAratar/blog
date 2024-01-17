from django.urls import path
from .views import *

urlpatterns = [
    path('article/', ArticleListAPIView.as_view()),
    path('article/create/', ArticleListCreateAPIView.as_view()),
    path('article/crud/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view()),
]

