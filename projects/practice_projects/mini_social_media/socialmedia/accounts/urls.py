from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.Register,name="Register"),
    path("login/",views.User_login,name="User_login"),
    path("profile_view/",views.profile_view , name = "profile_view"),

]