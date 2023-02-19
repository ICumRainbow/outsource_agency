import telegram
from django.conf import settings
from telegram.constants import ParseMode

from contact_bot.models import TelegramUser


async def send_message(message: str) -> None:
    """
    Accepts message as parameter and sends it to specified chat_id.
    :param message:
    """
    bot = telegram.Bot(token=settings.TELEGRAM['TOKEN'])
    users = TelegramUser.objects.all()
    async for user in users:
        await bot.send_message(chat_id=user.chat,
                           text=message, parse_mode=ParseMode.HTML)
