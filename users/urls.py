from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import UserCreateApiView, UserListApiView

app_name = UsersConfig.name

urlpatterns = [
    path("create/", UserCreateApiView.as_view(), name="user_create"),
    path("list/", UserListApiView.as_view(), name="user_list"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
