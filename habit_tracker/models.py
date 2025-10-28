from django.db import models

from config import settings


class Habit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        help_text="Укажите владельца",
        related_name="habit",
        blank=True,
        null=True,
    )
    place = models.CharField(
        max_length=150,
        verbose_name="Место, в котором необходимо выполнять привычку",
        help_text="Укажите место, в котором необходимо выполнять привычку",
    )
    time = models.DateTimeField(
        verbose_name="Время, когда необходимо выполнять привычку",
        help_text="Укажите время, когда необходимо выполнять привычку",
    )
    action = models.CharField(
        verbose_name="Действие, которое представляет собой привычка",
        help_text="Укажите действие, которое представляет собой привычка",
    )
    is_pleasant_habit = models.BooleanField(
        verbose_name="Признак приятной привычки", help_text="Укажите признак приятной привычки", default=False
    )
    associated_habit = models.CharField(
        max_length=150,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        blank=True,
        null=True,
    )
    periodicity = models.PositiveIntegerField(
        verbose_name="Периодичность", help_text="Укажите периодичность", default=1
    )
    reward = models.CharField(max_length=150, verbose_name="Вознаграждение", help_text="Укажите вознаграждение", blank=True, null=True)
    time_complete = models.DurationField(verbose_name="Время на выполнение в секундах", help_text="Укажите время на выполнение в секундах")
    is_publish = models.BooleanField(verbose_name="Признак публичности", help_text="Укажите признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return self.action
