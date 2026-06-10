### A router automatically creates URLs for your API.

instead of writing this manually:
path('users/', views.user_list),
path('users/<int:id>/', views.user_detail),

You just write:
router.register('users', UserViewSet)
✅ And Django automatically creates all routes.






# 🔹 3. Basic Router Example (IMPORTANT)
✅ Code:
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = router.urls


🔍 What each line does:
1. Create router
router = routers.SimpleRouter()
👉 Creates a router object.

2. Register users
router.register(r'users', UserViewSet)
users → URL prefix
UserViewSet → logic

3. Register accounts
router.register(r'accounts', AccountViewSet)

4. Add URLs
urlpatterns = router.urls
👉 This tells Django:
“Use all routes created by router”

# 🔹 4. Automatically Generated URLs
For:
router.register('users', UserViewSet)
✅ Generated routes:
URL	Method	Action
/users/	GET	list all users
/users/	POST	create user
/users/{id}/	GET	get one user
/users/{id}/	PUT	update
/users/{id}/	PATCH	partial update
/users/{id}/	DELETE	delete


# 5. register() Arguments
Mandatory:
router.register(prefix, viewset)

Argument            	Meaning
prefix	                URL name (users, accounts)
viewset	                Class handling logic

Optional:
router.register('users', UserViewSet, basename='user')
👉 Used when queryset is missing.

❗ Why basename needed?
If you don't have:
queryset = User.objects.all()
Then Django can't guess model name → error.


# 6. Using include()
✅ Method 1 (append)
urlpatterns = [
    path('forgot-password/', ForgotPasswordView.as_view()),
]
urlpatterns += router.urls

✅ Method 2 (include)
from django.urls import include
urlpatterns = [
    path('', include(router.urls)),
]

✅ Method 3 (with prefix)
urlpatterns = [
    path('api/', include(router.urls)),
]
👉 Now URLs become:
/api/users/
/api/accounts/