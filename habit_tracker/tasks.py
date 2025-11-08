from celery import shared_task
import requests

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


@shared_task
def send_telegram(text, chat_id):
    """Функция отправляет сообщения в телеграм BOT"""

    params = {
        "text": text,
        "chat_id": chat_id
    }

    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)
