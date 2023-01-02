from django.conf import settings
from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)
    chat = models.IntegerField()
