from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(UserAdmin):
    """
    Настройки отображения в административной панели для модели пользователей.
    """
    pass
