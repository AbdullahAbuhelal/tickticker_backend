from django.db import models
from abstract.models import BaseModel

class SavedTicker(BaseModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=255)
