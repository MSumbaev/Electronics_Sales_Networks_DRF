from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUser
from users.serializers import UserRegisterSerializer, UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создание юзера"""
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт вывода информации о юзере"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт обновления юзера"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsUser]
