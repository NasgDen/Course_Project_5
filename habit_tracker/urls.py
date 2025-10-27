from django.urls import path

from .apps import HabitTrackerConfig
from .views import HabitCreateApiView, HabitListApiView, HabitUpdateApiView, HabitDeleteAPIView

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("list/", HabitListApiView.as_view(), name="habit_list"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="habit_update"),
    path("retrieve/<int:pk>/", HabitUpdateApiView.as_view(), name="habit_retrieve"),
    path("delete/<int:pk>/", HabitDeleteAPIView.as_view(), name="habit_delete"),
]