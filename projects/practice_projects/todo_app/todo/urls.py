from django.urls import path
from . import views

app_name = 'todo'
urlpatterns=[
    path('',views.task_list,name='task_list'),
    path('add/',views.task_edit,name='task_edit'),
    path('edit/<int:pk>/',views.task_upadate,name='task_upadate'),
    path('delete/<int:pk>/',views.task_delete,name='task_delete'),
    path('toggle/<int:pk>/',views.task_toggle_complete,name='task_toggle_complete'),

]