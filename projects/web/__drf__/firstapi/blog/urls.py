from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('list_book',views.books_list,name='books_list'),
    path('add_book/',views.add_book,name='add_book'),
    path('update_book/<int:pk>/',views.update_book,name="update_book"),
    path('delete_book/<int:pk>/',views.delete_book,name="delete_book"),
]

