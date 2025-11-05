import json
from datetime import datetime, timedelta

from celery import shared_task
import celery.schedules
from datetime import date
import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN

from django_celery_beat.models import PeriodicTask, IntervalSchedule, PeriodicTasks

from .models import Habit


def send_message_habit():
    for habit in Habit.objects.all():
        if habit.owner.tg_chat_id is not None:
            print(habit.owner.tg_chat_id)
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}"
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=f"{habit.periodicity}",
                period=IntervalSchedule.DAYS,
            )
            PeriodicTask.objects.create(
                interval=schedule,
                name=f"{habit.action}",
                start_time=habit.time,
                task="habit_tracker.tasks.send_telegram",
                args=json.dumps([message, habit.owner.tg_chat_id])
            )


@shared_task
def send_telegram(text, chat_id):
    """Функция отправляет сообщения в телеграм BOT"""
    print("Выполнение функции по отправке сообщения")
    params = {
        "text": text,
        "chat_id": chat_id
    }

    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
