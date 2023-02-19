from django.conf import settings
from django.db import models


from core.models import BaseModel


class TelegramUser(BaseModel):
    user = models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    chat = models.IntegerField(verbose_name='Chat ID')
    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'chat'], name='unique_user_chat_combination'
            )
        ]

    def __str__(self):
        return self.user.__str__()

    def __repr__(self):
        return f"TelegramUser(user='{self.user}', chat='{self.chat}')"



