from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, nickname, password=None, **extra_fields):
        if not nickname:
            raise ValueError("Nickname is required")
        user = self.model(nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, nickname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(nickname, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nickname

