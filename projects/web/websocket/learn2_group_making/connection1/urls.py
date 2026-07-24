from django.urls import path
from .views import UserAuthViewSet

urlpatterns = [ 
    path("register/",UserAuthViewSet.as_view({"post": "register"}),name="register"),
    path("login/",UserAuthViewSet.as_view({"post": "login"}),name="login"),
   
]