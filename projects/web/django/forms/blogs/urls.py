from django.urls import path
from . import views

urlpatterns=[
    path('',views.contact,name="Contact"),
    path('submit/',views.submit,name="submitdata")

]