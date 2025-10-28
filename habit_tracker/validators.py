from datetime import timedelta

from rest_framework.serializers import ValidationError

class TimeValidator:
    """Класс реализует валидацию поля time_complete модели Habit"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        print("VALUE:", dict(value).get(self.field))
        if dict(value).get(self.field) > timedelta(seconds=120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")

