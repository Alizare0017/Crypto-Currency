from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from django.conf import settings


class User(AbstractUser):
    COMMON = "COMMON"
    PERMIUM = "PREMIUM"
    role_choices = (
        (PERMIUM, "premium"),
        (COMMON, "common")
    )
    phone = models.CharField(
        max_length=13, validators=[RegexValidator(regex=settings.PHONE_REGEX)], null=True, blank=True
    )
    role = models.CharField(max_length=8, choices=role_choices, null=True, blank=True)

    is_phone_activated = models.BooleanField(default=False)
    is_email_activated = models.BooleanField(default=False)

    @property
    def is_permium(self):
        return self.role == self.PERMIUM

    @property
    def is_common(self):
        return self.role == self.COMMON

    @property
    def full_name(self):
        return self.first_name + self.last_name