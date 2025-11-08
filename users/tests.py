import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тест - Создание пользователя"""

        url = reverse("users:user_create")
        data = {
            "email": "user1@mail.ru",
            "username": "user",
            "phone": "123456789",
            "city": "NY",
            "tg_chat_id": 111111111,
            "password": "test123456789"
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)
