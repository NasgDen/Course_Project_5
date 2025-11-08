import json

from django_celery_beat.models import IntervalSchedule, PeriodicTask


def add_task_habit(habit):
    """Функция добавляет отложенную задачу для Celery"""

    if (
        habit.owner.tg_chat_id is not None
        and not PeriodicTask.objects.filter(name=f"{habit.owner.email}_{habit.action}").exists()
    ):
        message = f"Я буду {habit.action} в {habit.time} в {habit.place}"
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=f"{habit.periodicity}",
            period=IntervalSchedule.DAYS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name=f"{habit.owner.email}_{habit.action}",
            start_time=habit.time,
            task="habit_tracker.tasks.send_telegram",
            args=json.dumps([message, habit.owner.tg_chat_id]),
        )
