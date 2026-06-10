from . import views
from django.urls import path

urlpatterns = [
    path('blogs', views.names, name='bloghome'),
]


