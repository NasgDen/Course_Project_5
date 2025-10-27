from django.urls import path

from .apps import UsersConfig
from .views import UserCreateApiView, UserListApiView

app_name = UsersConfig.name

urlpatterns = [
    path("create/", UserCreateApiView.as_view(), name="user_create"),
    path("list/", UserListApiView.as_view(), name="user_list"),
]
