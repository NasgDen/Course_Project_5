from datetime import timedelta

from rest_framework.serializers import ValidationError


class TimeValidator:
    """Класс реализует валидацию поля time_complete модели Habit"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        print("Время:", dict(value).get(self.field))
        if dict(value).get(self.field) is not None:
            if dict(value).get(self.field) > timedelta(seconds=120):
                raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class PeriodicityValidator:
    """Класс реализует валидацию поля periodicity модели Habit"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field) is not None:
            if dict(value).get(self.field) > 7:
                raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")


class AssociatedRewardValidator:
    """
    Класс реализует валидацию - Исключить одновременный выбор связанной привычки и указания вознаграждения модели Habit
    """

    def __call__(self, value):
        if dict(value).get("associated_habit") is not None and dict(value).get("reward") is not None:
            raise ValidationError("Нельзя одновременно выбрать связанную привычку и вознаграждение")


class IsPleasantValidator:
    """
    Класс реализует валидацию поля is_pleasant модели Habit
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        print(dict(value).get("associated_habit"))
        if bool(dict(value).get(self.field)) and (
            dict(value).get("associated_habit") is not None or dict(value).get("reward") is not None
        ):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class AssociatedHabitValid:
    """
    В связанные привычки могут попадать только привычки с признаком приятной привычки.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get("associated_habit") is not None:
            associated_habit = dict(value).get("associated_habit")
            if not associated_habit.is_pleasant_habit:
                raise ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки."
                )
