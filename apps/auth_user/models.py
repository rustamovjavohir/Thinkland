from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_client(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_client', True)
        extra_fields.setdefault('is_active', True)
        if email:
            email = email.lower()
        return self.create_user(username, email, password, **extra_fields)

    def create_staff(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to='user/profile_photos',
                                      null=True, blank=True,
                                      verbose_name='Фото профиля',
                                      default='user/profile_photos/default.png')
    is_client = models.BooleanField(default=False,
                                    verbose_name='Клиент')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    objects = UserManager()


class Authors(BaseModel):
    name = models.CharField(max_length=255,
                            verbose_name='Имя автора')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name
