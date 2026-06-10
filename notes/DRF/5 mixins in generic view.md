# 👉 Generic Views = ready-made full solution
# 👉 Mixins = small pieces you combine to build your own solution

# 🧠 Simple Analogy
Generic View 🍔 → Ready burger (just eat)
Mixins 🧱 → Ingredients (you cook yourself)



🔥 1. GENERIC VIEW (Easy Way)
Using Django REST Framework

# ✅ Code (Generic View)
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# 🧾 What this code does
👉 This ONE class automatically:
GET → show all books
POST → create new book
👉 You don’t write any method manually 😎

🖥️ Output
GET /books/
[
  {
    "id": 1,
    "title": "Python",
    "author": "John",
    "publish_date": "2024-01-01"
  }
]

POST /books/
{
  "title": "Django",
  "author": "Alice",
  "publish_date": "2025-01-01"
}

⚙️ Explanation (Simple)
ListCreateAPIView already has:
.list() (GET)
.create() (POST)

👉 That’s why code is short.











###### ################ 🚀 2. MIXINS (Manual Control Way)
✅ Code (Mixins)

class profileshow(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def get(self,request ):
        return self.list(request )

class profileadd(mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def post(self,request, *args, **kwargs):
        return self.create(request ,*args, **kwargs)

class profilesingle(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class profileupdate(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    


class profiledelete(mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = profiles.objects.all()
    serializer_class = aboutprofile

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 🧾 What this code does
👉 Same functionality as Generic View:
GET → list books
POST → create book

# 👉 BUT:
You manually connect methods
🖥️ Output (Same as above)
GET /books/
[
  {
    "id": 1,
    "title": "Python",
    "author": "John",
    "publish_date": "2024-01-01"
  }
]

# ⚙️ Explanation (Very Simple)
ListModelMixin → gives .list()
CreateModelMixin → gives .create()
GenericAPIView → base class

👉 You connect them:

def get(self, request):
    return self.list(request)



###### Mixins methods
| Mixin                | Method it provides | HTTP Method |
| -------------------- | ------------------ | ----------- |
| `ListModelMixin`     | `.list()`          | GET         |
| `CreateModelMixin`   | `.create()`        | POST        |
| `RetrieveModelMixin` | `.retrieve()`      | GET         |
| `UpdateModelMixin`   | `.update()`        | PUT / PATCH |
| `DestroyModelMixin`  | `.destroy()`       | DELETE      |






##### Example
from rest_framework import mixins, generics

class BookView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)   # from ListModelMixin

    def post(self, request):
        return self.create(request) # from CreateModelMixin