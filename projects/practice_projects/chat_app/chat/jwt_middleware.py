from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth import get_user_model

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class JWTAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):

        headers = dict(scope["headers"])

        authorization = headers.get(b"authorization")

        scope["user"] = AnonymousUser()

        if authorization:

            try:

                auth = authorization.decode()

                if auth.startswith("Bearer "):

                    token = auth.split(" ")[1]

                    access_token = AccessToken(token)

                    user = await get_user(access_token["user_id"])

                    scope["user"] = user

            except Exception as e:
                print(e)

        return await self.app(scope, receive, send)

def JWTAuthMiddlewareStack(app):
        return JWTAuthMiddleware(app)