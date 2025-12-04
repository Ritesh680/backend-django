from rest_framework import generics
from .models import User
from .serializer import UserCreateSerializer, UserLoginSerializer, UserSerializer


# ListAPIView automatically handles GET requests and returns a list of items
class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
