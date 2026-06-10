from django.urls import path
from . import views

urlpatterns = [
    path('', views.abouts.as_view(), name='abouts'),
    # You need this second line to pass the 'pk' to your put and delete methods
    path('<int:pk>/', views.abouts.as_view(), name='abouts_detail'),
]
