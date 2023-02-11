from django.contrib import admin

# Register your models here.
from contact_bot.models import TelegramUser


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'chat']
