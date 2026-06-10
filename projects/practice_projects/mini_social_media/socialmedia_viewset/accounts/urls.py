from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, ProfileViewSet

router = DefaultRouter()
router.register('auth', AuthViewSet, basename='auth')
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = router.urls