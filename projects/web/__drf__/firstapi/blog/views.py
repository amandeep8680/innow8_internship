from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import Bookinfo

def home(request):
    return render(request,'index.html')


@api_view(['GET'])
def books_list(request):
    if request.method == 'GET':
        books=Book.objects.all()
        serializer= Bookinfo(books,many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
def add_book(request):
    if request.method == 'POST':
        serializer = Bookinfo(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT'])
def update_book(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book Not Found'},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = Bookinfo(book)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = Bookinfo(book , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','DELETE'])
def delete_book(request,pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error':'Book Not Found'},status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        serializer = Bookinfo(book)
        return Response(serializer.data)

    elif request.method=='DELETE':
        book.delete()
        return Response({'message' : 'Book Deleted Successfully'}, status=status.HTTP_200_OK)
    