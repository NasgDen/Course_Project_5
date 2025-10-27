from django.shortcuts import render
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    """Класс реализует интерфейс для создания пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password())
        user.save()
