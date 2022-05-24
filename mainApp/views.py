from rest_framework import generics
from .models import Book, Journal
from .serializers import BookSerializer, JournalSerializer
from rest_framework import viewsets

class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class JournalListAPIView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

# class BookViewSet(viewsets.ViewSet):
#     def list(self, request):
#         data = Book.objects.all()
#         serializer = BookSerializer(data,many=True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk=None):
#         data = Book.objects.filter(id=pk)
#         serializer = BookSerializer(data,many=True)
#         return Response(serializer.data)


# class JournalViewSet(viewsets.ViewSet):
#     def list(self, request):
#         data = Journal.objects.all()
#         serializer = JournalSerializer(data,many=True)
#         return Response(serializer.data)

#     def retrieve(self,request,pk=None):
#         data = Journal.objects.filter(id=pk)
#         serializer = JournalSerializer(data,many=True)
#         return Response(serializer.data)

        
