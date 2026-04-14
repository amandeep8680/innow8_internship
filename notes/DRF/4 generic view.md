generic views is a readymade view that does common task for you

## Without Generic
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

## With Generic View (Easy Way)
from django.views.generic import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'students.html'


# html template is same for both 


# methods

# ListAPIView
👉 Only shows list of data
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

✔ Method used: GET

# ➕ 2. CreateAPIView
👉 Only creates new data
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
✔ Method used: POST

# 🔍 3. RetrieveAPIView
👉 Get single object
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
✔ Method used: GET (single item)

# ✏️ 4. UpdateAPIView
👉 Update data
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
✔ Methods used:
PUT
PATCH

# ❌ 5. DestroyAPIView
👉 Delete data
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
✔ Method used: DELETE


# Example (Real Understanding)
class BookAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
👉 This ONE class can:
Show book 📖
Update book ✏️
Delete book ❌







#####  ######### EXAMPLE COMPLETE CODE   #####  #########
# Model (Book)
models.py
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()

    def __str__(self):
        return self.title



# 2. Serializer

serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


        
# 3. Generic API Views (CRUD)
views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# 1. List all books + Create new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# 2. Retrieve single book + Update + Delete
class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

