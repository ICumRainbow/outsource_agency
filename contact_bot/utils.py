import telegram
from django.conf import settings
from telegram.constants import ParseMode

from contact_bot.models import TelegramUser


async def send_message(message: str) -> None:
    """
    Accepts message as parameter and sends it to specified chat_id.
    :param message:
    """
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['TOKEN'])
    users = TelegramUser.objects.all()
    async for user in users:
        await bot.send_message(chat_id=user.chat,
                           text=message, parse_mode=ParseMode.HTML)
