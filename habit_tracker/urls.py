from django.urls import path

from .apps import HabitTrackerConfig
from .views import HabitCreateApiView, HabitListApiView

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("create/", HabitCreateApiView.as_view(), name="habit_create"),
    path("list/", HabitListApiView.as_view(), name="habit_list"),
]