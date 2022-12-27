import telegram  # this is from python-telegram-bot package

from django.conf import settings
from django.template.loader import render_to_string


def send_message(message: str) -> None:
    """
    Accepts message as parameter and sends it to specified chat_id.
    :param message:
    """
    # message_html = render_to_string('telegram_message.html', {
    #     'event': event
    # })
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['TOKEN'])
    bot.send_message(chat_id="86494096",
                     text=message, parse_mode=telegram.ParseMode.HTML)
