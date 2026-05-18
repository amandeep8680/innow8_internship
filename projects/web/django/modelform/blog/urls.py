from django.urls import path
from . import views

urlpatterns=[
    path('',views.create_student, name='create_student'),
    path('list',views.show_list,name='show_list'),
    path('details/<int:pk>/', views.student_detail,name='student_detail'),
    path('update/<int:pk>/', views.update,name='update'),
    path('delete/<int:pk>/', views.delete,name='delete'),

]
