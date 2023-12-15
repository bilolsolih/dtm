from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.accounts import choices
from apps.accounts.managers import UserManager
from apps.common.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    # AUTHENTICATION FIELDS #
    username = models.CharField(_('Foydalanuvchi nomi'), max_length=64, unique=True)
    phone_number = models.CharField(_('Telefon raqami'), max_length=15, unique=True)
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)
    is_verified = models.BooleanField(_('Tekshirilganlik statusi'), default=False)
    is_active = models.BooleanField(_('Faollik statusi'), default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # PERSONAL INFO #
    full_name = models.CharField(_('Ism Sharif'), max_length=128)
    photo = models.ImageField(_('Akkaunt uchun rasm'), upload_to='images/accounts/%Y/%m/', blank=True, null=True)
    birthdate = models.DateField(_('Tug\'ilish sanasi'), null=True)
    gender = models.CharField(_('Erkak yoki Ayol'), max_length=6, choices=choices.GENDERS)

    # DISTINCT FIELDS #
    type = models.CharField(_('O\'quvchi, O\'qituvchi yoki Administrator'), max_length=1, choices=choices.USERS)
    is_staff = models.BooleanField(_('Xodimlik statusi'), default=False)

    # PREFERENCES #

    # OTHERS #
    objects = UserManager()

    class Meta:
        verbose_name = _('Akkaunt')
        verbose_name_plural = _('Akkauntlar')
        indexes = [
            models.Index(fields=['phone_number']),
            models.Index(fields=['username']),
            models.Index(fields=['full_name'])
        ]

    @property
    def get_age(self):
        return timezone.now() - self.birthdate

    def __str__(self):
        return f"{self.type} - {self.full_name}"


__all__ = ['User']
