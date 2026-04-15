from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profiles',views.profileshow,basename='profiles')

urlpatterns = [
    path('', include(router.urls)),
]




# manual
# from django.urls import path
# from .views import ProfileViewSet

# profile_list = ProfileViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# profile_detail = ProfileViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })

# urlpatterns = [
#     path('profiles/', profile_list),
#     path('profiles/<int:pk>/', profile_detail),
# ]