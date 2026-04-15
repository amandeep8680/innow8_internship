#### Viewset is basically a class that handles multiple api actions in one place

Instead of writing separate views like:
get users
create user
update user
delete user
# 👉 You write ONE class that does everything

## Important Concept
❗ ViewSets do NOT use .get() or .post()


| HTTP Method  | Action Name        |
| ------------ | ------------------ |
| GET (list)   | `list()`           |
| GET (single) | `retrieve()`       |
| POST         | `create()`         |
| PUT          | `update()`         |
| PATCH        | `partial_update()` |
| DELETE       | `destroy()`        |


## Example (Simple)
class UserViewSet(ViewSet):

    def list(self, request):
        # return all users

    def retrieve(self, request, pk=None):
        # return single user

## How URLs are created?

👉 You DON'T manually write URLs
👉 Use a Router

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
✅ Automatically creates:
GET     /users/        → list
GET     /users/1/      → retrieve
POST    /users/        → create
PUT     /users/1/      → update
DELETE  /users/1/      → delete     


Manually creates
profile_list = ProfileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

profile_detail = ProfileViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('profiles/', profile_list),
    path('profiles/<int:pk>/', profile_detail),
]



##  Best Shortcut: ModelViewSet
👉 Instead of writing all methods manually, use:
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

🎉 Done! You get ALL actions automatically:
list
create
retrieve
update
delete


## Types of ViewSets
1. ViewSet
👉 Basic (you write everything yourself)

2. GenericViewSet
👉 Gives helper functions like:
get_queryset()
get_object()
But ❌ no actions

3. ModelViewSet ⭐ (Most used)
👉 Full CRUD already built-in

4. ReadOnlyModelViewSet
👉 Only:
list
retrieve
❌ No create/update/delete




# Example
model and serializer is same as generic_api and generic_Api mixin

view.py
from rest_framework import viewsets
from .serializers import aboutprofile
from .models import profiles

class profileshow(viewsets.ModelViewSet):
    queryset= profiles.objects.all()
    serializer_class=aboutprofile

urls.py
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profiles',views.profileshow,basename='profiles')

urlpatterns = [
    path('', include(router.urls)),
]

 # manual
 from django.urls import path
 from .views import ProfileViewSet
 profile_list = ProfileViewSet.as_view({
     'get': 'list',
     'post': 'create'
 })

 profile_detail = ProfileViewSet.as_view({
     'get': 'retrieve',
     'put': 'update',
     'delete': 'destroy'
 })

 urlpatterns = [
     path('profiles/', profile_list),
     path('profiles/<int:pk>/', profile_detail),
 ]





 