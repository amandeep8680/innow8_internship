from django.urls import path
from . import views
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students',StudentViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     # path('students/', views.StudentList),
#     path('students/', views.Studentcreateandlist),
#     path('students/edit/<int:pk>/', views.studentedit),
# ]

