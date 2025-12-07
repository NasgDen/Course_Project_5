from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit_tracker.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            owner=self.user,
            place="Спортзал",
            time="2025-11-08T12:10:00Z",
            action="Подтягиваться",
            is_pleasant_habit=False,
            periodicity=3,
            time_complete="00:00:40",
            is_publish=True
        )

    def test_habit_retrieve(self):
        """Тест - детальный просмотр привычки"""

        url = reverse("habit_tracker:habit_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("action"), self.habit.action)
        self.assertEqual(data.get("is_pleasant_habit"), self.habit.is_pleasant_habit)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)
        self.assertEqual(data.get("time_complete"), self.habit.time_complete)
        self.assertEqual(data.get("is_publish"), self.habit.is_publish)

    def test_habit_create(self):
        """Тест - Создание привычки"""

        url = reverse("habit_tracker:habit_create")
        data = {
            "owner": self.user.pk,
            "place": "Спортзал",
            "time": "2025-11-08T12:30:00Z",
            "action": "Отжиматься",
            "is_pleasant_habit": False,
            "periodicity": 3,
            "time_complete": "00:01:20",
            "is_publish": False,
                }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update_patch(self):
        """Тест - Изменение привычки. Patch запрос"""
        url = reverse("habit_tracker:habit_update", args=(self.habit.pk,))
        data = {
            "action": "Бегать",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update_put(self):
        """Тест - Изменение привычки. Put запрос"""
        url = reverse("habit_tracker:habit_update", args=(self.habit.pk,))
        data = {
            "owner": self.user.pk,
            "place": "Дом",
            "time": "2025-11-08T12:30:00Z",
            "action": "Учиться",
            "is_pleasant_habit": False,
            "periodicity": 1,
            "time_complete": "00:01:20",
            "is_publish": False,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        """Тест - Удаление привычки."""
        url = reverse("habit_tracker:habit_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тест - Вывод привычек."""

        url = reverse("habit_tracker:habit_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [{
                'action': 'Подтягиваться',
                'associated_habit': None,
                'id': 4,
                'is_pleasant_habit': False,
                'is_publish': True,
                'owner': 3,
                'periodicity': 3,
                'place': 'Спортзал',
                'reward': None,
                'time': '2025-11-08T15:10:00+03:00',
                'time_complete': '00:00:40'}]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_publish_list(self):
        """Тест - Вывод публичных привычек."""

        url = reverse("habit_tracker:habit_publish")
        response = self.client.get(url)
        data = response.json()
        result = [
            {
                "id": 5,
                "place": "Спортзал",
                "time": "2025-11-08T15:10:00+03:00",
                "action": "Подтягиваться",
                "is_pleasant_habit": False,
                "periodicity": 3,
                "reward": None,
                "time_complete": "00:00:40",
                "is_publish": True,
                'associated_habit': None,
                "owner": 4,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
