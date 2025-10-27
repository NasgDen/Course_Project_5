from django.shortcuts import render
from rest_framework import generics

from habit_tracker.models import Habit
from habit_tracker.serializers import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    """Класс реализует интерфейс для создания данных о привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListApiView(generics.ListAPIView):
    """Класс реализует интерфейс для вывода всех привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(generics.UpdateAPIView):
    """Класс реализует интерфейс для изменения данных о привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Класс реализует интерфейс для отображения данных об одной привычке"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Класс реализует интерфейс для удаления данных о привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
