# # urls.py
# from django.urls import path
# from . import views 

# urlpatterns = [
#      path('', views.home),
#     path('books/', views.book_list,name="books"),
#     path('book/<int:pk>',views.book_detail,name='books')
# ]

from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path('books/', book_list.as_view(), name='book-list-create'),
    path('books/<int:pk>/', book_detail.as_view(), name='book-detail'),
] 