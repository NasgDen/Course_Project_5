from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    """Класс реализует интерфейс для создания пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListApiView(generics.ListAPIView):
    """Класс реализует интерфейс для просмотра пользователей"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
