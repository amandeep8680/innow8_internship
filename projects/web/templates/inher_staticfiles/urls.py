from django.urls import path
from . import views

urlpatterns = [
    # path('',views.base,name="Inheritance & Static files"),
    path('',views.home,name="home"),
    path('about/',views.about,name="about")


]