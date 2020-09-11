from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField('О себе', blank=True, null=True)

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLE_CHOICES = ((ADMIN, 'Администратор'), (MODERATOR, 'Модератор'), (USER, 'Пользователь'))
    role = models.CharField('Группа', choices=ROLE_CHOICES, max_length=9, default=USER)
