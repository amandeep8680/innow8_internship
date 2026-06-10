from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import AuthViewSet, ProfileViewSet
from posts.views import PostViewSet

router = DefaultRouter()
router.register('auth', AuthViewSet, basename='auth')
router.register('profile', ProfileViewSet, basename='profile')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]