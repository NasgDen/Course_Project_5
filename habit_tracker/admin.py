from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "owner",
        "place",
        "time",
        "action",
        "is_pleasant_habit",
        "associated_habit",
        "periodicity",
        "reward",
        "time_complete",
        "is_publish",
    )
    list_filter = ("action",)
