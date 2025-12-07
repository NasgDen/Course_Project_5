import requests
from celery import shared_task

from config.settings import TELEGRAM_TOKEN, TELEGRAM_URL


@shared_task
def send_telegram(text, chat_id):
    """Функция отправляет сообщения в телеграм BOT"""

    params = {"text": text, "chat_id": chat_id}

    requests.get(f"{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage", params=params)
