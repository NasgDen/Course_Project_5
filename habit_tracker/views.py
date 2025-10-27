from django.shortcuts import render
from rest_framework import generics

from habit_tracker.models import Habit
from habit_tracker.serializers import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitListApiView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer