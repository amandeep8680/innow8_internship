from django.urls import path
from . import views

urlpatterns = [
    path('', views.profileshow.as_view(), name='profileshow'),
    path('add/', views.profileadd.as_view(), name='profileadd'),
    path('profilesingle/<int:pk>/', views.profilesingle.as_view(), name='profilesingle'),
    path('profileupdate/<int:pk>/', views.profileupdate.as_view(), name='profileupdate'),
    path('profiledelete/<int:pk>/', views.profiledelete.as_view(), name='profile_detail'),
]
