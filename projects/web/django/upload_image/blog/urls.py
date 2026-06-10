from django.urls import path
from . import views

urlpatterns=[
    path('upload/',views.uploads,name='uploads'),
    path('profile/',views.view_profiles,name='view_profiles'),
    path('/delete/<int:pk>',views.delete,name='delete')

]