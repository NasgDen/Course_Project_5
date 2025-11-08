from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics

from habit_tracker.models import Habit
from habit_tracker.pagination import HabitPagination
from habit_tracker.permissions import IsOwner
from habit_tracker.serializers import HabitSerializer
from habit_tracker.services import add_task_habit


# from habit_tracker.tasks import send_message_habit


class HabitCreateApiView(generics.CreateAPIView):
    """Класс реализует интерфейс для создания данных о привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()
        add_task_habit(habit)


class HabitListApiView(generics.ListAPIView):
    """Класс реализует интерфейс для вывода всех привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination


    def get_queryset(self):
        queryset = Habit.objects.filter(Q(owner=self.request.user) |  Q(is_publish=True))
        return queryset


class HabitUpdateApiView(generics.UpdateAPIView):
    """Класс реализует интерфейс для изменения данных о привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Класс реализует интерфейс для отображения данных об одной привычке"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Класс реализует интерфейс для удаления данных о привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsOwner]


class HabitPublishListApiView(generics.ListAPIView):
    """Класс реализует интерфейс для вывода публичных привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        queryset = Habit.objects.filter(is_publish=True)
        return queryset