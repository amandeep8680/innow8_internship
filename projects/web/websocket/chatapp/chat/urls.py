from django.urls import path
from . import views
urlpatterns=[
    path('register/',views.Register,name='register'),
    path('login/',views.login,name='login'),
    path('contacts/',views.contacts,name='contacts'),
    path('chats',views.chats,name='chats'),
    path('chat/<pk>/',views.contact_chat,name='contact_chat'),
    path('start-chat/', views.start_chat),
]