from rest_framework import serializers
from .models import Book, Journal

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'num_pages', 'genre')

class JournalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Journal
        fields = ('id', 'types', 'publisher')