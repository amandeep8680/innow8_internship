create normal model
instead of forms we use serializer


-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-model-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-
from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title


-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-create serializers.py-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-
same as forms the difference is serializer imnsteam of forms



#projects/web/__drf__/a_intro/blog/serializers.py
from rest_framework  import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'







-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-views-=-=-=-=-=-=-=-=-==-=-=-=-=-=--=-=-=-

from django.shortcuts import render
from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


def home(request):
    return render(request,'books.html')


class book_list(APIView):

    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

# 🔹 LIST + CREATE
@api_view(['GET', 'POST'])
def book_list(request):

    # ✅ GET → List all books
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # ✅ POST → Create new book
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 🔹 RETRIEVE + UPDATE + DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Book Not Found'}, status=status.HTTP_404_NOT_FOUND)

    # ✅ GET → Single book
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # ✅ PUT → Update book
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ DELETE → Delete book
    elif request.method == 'DELETE':
        book.delete()
        return Response({'message': 'Book Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)    