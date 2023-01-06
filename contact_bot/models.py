from django.conf import settings
from django.db import models


# Create your models here.
class TelegramUser(models.Model):
    user = models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat = models.IntegerField(verbose_name='Chat ID')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'chat'], name='unique_user_chat_combination'
            )
        ]
