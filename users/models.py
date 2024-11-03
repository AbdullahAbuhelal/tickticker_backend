from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from abstract.models import BaseModel, BaseModelWithUUID

class User(AbstractUser, BaseModel, BaseModelWithUUID):
    username = None
    first_name = None
    last_name = None

    email = models.EmailField(db_index=True, null=False, blank=False, verbose_name=_("email"), unique=True)
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name=_("name"))


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):

        return f"{self.name} : {self.email}"