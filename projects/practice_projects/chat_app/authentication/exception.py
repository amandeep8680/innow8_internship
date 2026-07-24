from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidCredentials(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Invalid username or password."
    default_code = "invalid_credentials"


class UserAlreadyExists(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "User already exists."
    default_code = "user_exists"


class UserNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "User not found."
    default_code = "user_not_found"