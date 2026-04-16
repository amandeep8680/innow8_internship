from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post,name="create_post"),
    path('', views.get_posts,name="get_posts"),
    path('delete/<int:id>/', views.delete_post,name="delete_post"),
]