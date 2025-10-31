from rest_framework import serializers

from habit_tracker.models import Habit
from habit_tracker.validators import (AssociatedRewardValidator, IsPleasantValidator, PeriodicityValidator,
                                      TimeValidator, AssociatedHabitValid)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            TimeValidator(field="time_complete"),
            PeriodicityValidator(field="periodicity"),
            AssociatedRewardValidator(),
            IsPleasantValidator(field="is_pleasant_habit"),
            AssociatedHabitValid(field="associated_habit")
        ]
