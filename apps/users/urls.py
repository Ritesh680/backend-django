from django.urls import path
from .views import UserListAPI, UserCreateAPI, UserLoginAPI

urlpatterns = [
    path("users/", UserListAPI.as_view(), name="user-list"),
    path("users/create", UserCreateAPI.as_view(), name="user-create"),
    path("users/login", UserLoginAPI.as_view(), name="user-login"),
]
