from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post,name="create_post"),
    path('', views.get_posts,name="get_posts"),
    path('delete/<int:id>/', views.delete_post,name="delete_post"),
    path('like_count/<int:pk>/', views.like_count,name="like_count"),
    path('like_unlike/<int:pk>/', views.like_unlike,name="like_unlike"),
    path('comment/<int:pk>/', views.comment,name="comment"),

]