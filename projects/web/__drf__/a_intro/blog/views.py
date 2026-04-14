# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import Book
# # from .serializers import BookSerializer

# # @api_view(['GET'])
# # def book_list(request):
# #     books = Book.objects.all()
# #     serializerss = BookSerializer(books, many=True)
# #     return Response(serializerss.data)


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Book
# from .serializers import BookSerializer

# # @api_view(['GET', 'POST'])
# # def book_list(request):
    
# #     if request.method == 'GET':
# #         books = Book.objects.all()
# #         serializer = BookSerializer(books, many=True)
# #         return Response(serializer.data)

# #     elif request.method == 'POST':
# #         serializer = BookSerializer(data=request.data)
        
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','POST'])
# def book_list(request):

#     if request.method == 'GET':
#         books=Book.objects.all()
#         serializer=BookSerializer(books,many=True)
#         return Response(serializer.data)

#     elif request.method=='POST':
#         serializer=BookSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)

# @api_view(['PUT','DELETE'])
# def book_detail(request,pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({'error':'Book Not Found'} , status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         serializer = BookSerializer(book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method=='DELETE':
#         book.delete()
#         return Response({'message':'Book Deleteed Successfully'},status=status.HTTP_202_ACCEPTED)
















# from django.shortcuts import render
# from rest_framework.decorators import api_view , APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Book
# from .serializers import BookSerializer


# def home(request):
#     return render(request,'books.html')


# class book_list(APIView):

#     def get(self,request):
#         books=Book.objects.all()
#         serializer=BookSerializer(books,many=True)
#         return Response(serializer.data)

# # 🔹 LIST + CREATE
# @api_view(['GET', 'POST'])
# def book_list(request):

#     # ✅ GET → List all books
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     # ✅ POST → Create new book
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 🔹 RETRIEVE + UPDATE + DELETE
# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):

#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response({'error': 'Book Not Found'}, status=status.HTTP_404_NOT_FOUND)

#     # ✅ GET → Single book
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     # ✅ PUT → Update book
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # ✅ DELETE → Delete book
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response({'message': 'Book Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)







from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# 1. List all books + Create new book
class book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 2. Retrieve single book + Update + Delete
class book_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer