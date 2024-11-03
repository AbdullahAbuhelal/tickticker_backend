from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created_at"))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_("updated_at"))

    class Meta:
        abstract = True

class BaseModelWithUUID(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4(), primary_key=True, editable=False, verbose_name=_("id")
    )

    class Meta:
        abstract = True