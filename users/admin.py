from django.contrib import admin

from users.models import User


@admin.register(User)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "city",
        "avatar",
        "tg_chat_id",
    )
    list_filter = ("email",)

