from datetime import timedelta

from rest_framework.serializers import ValidationError

class TimeValidator:
    """Класс реализует валидацию поля time_complete модели Habit"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class PeriodicityValidator:
    """Класс реализует валидацию поля periodicity модели Habit"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")


class AssociatedRewardValidator:
    """
    Класс реализует валидацию - Исключить одновременный выбор связанной привычки и указания вознаграждения модели Habit
    """

    def __call__(self, value):
        print(value)
        if dict(value).get("associated_habit") is not None and dict(value).get("reward") is not None:
            raise ValidationError("Нельзя одновременно выбрать связанную привычку и вознаграждение")
