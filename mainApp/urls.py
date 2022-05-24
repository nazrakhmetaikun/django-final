from django.contrib import admin
from django.urls import path, include
from .views import BookListAPIView, JournalListAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    # path('books/<int:id>', )
    path('journals/', JournalListAPIView.as_view())
]