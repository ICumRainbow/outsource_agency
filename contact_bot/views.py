import json

import telegram
from asgiref.sync import async_to_sync
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import MessageEntity

from contact_bot.context_processors import TelegramSigner
from contact_bot.models import TelegramUser

from contact_bot.utils import send_message

bot = telegram.Bot(token=settings.TELEGRAM['TOKEN'])


def parse_update(bot: telegram.Bot, request_token: str, request) -> telegram.Update:
    # noinspection GrazieInspection
    """
    First checks if the request came from Telegram.
    If so, parses telegram update and returns it.
    If not, raises forbidden http error.
    :param telegram.Bot bot: Bot instance
    :param str request_token: Token that was passed in request
    :param request: The actual request
    :return: Telegram update (if token is correct)
    :rtype: telegram.Update
    """
    # Abort request if it is not from telegram
    if bot.token != request_token:
        raise PermissionDenied('Token checking failed')

    # Parse telegram update from json
    update = telegram.Update.de_json(json.loads(request.body), bot)

    return update


# class TelegramBotView(View):
#     update = None
#
#     def post(self, request, *args, **kwargs):
#         token = kwargs.get('token')
#         self.update: telegram.Update = parse_update(bot, request_token=token, request=request)
#         return HttpResponse(self.update)


signer = TelegramSigner()


@csrf_exempt
def telegram_view(request, token):
    update: telegram.Update = parse_update(bot, request_token=token, request=request)
    message = update.message.text.split()

    if update.message.parse_entity(entity=MessageEntity(type='BOT_COMMAND', length=6, offset=0)) == '/start' and len(
            message) > 1:
        chat_id = update.message.chat_id
        text = 'Welcome!\nNow you will be receiving messages sent via contact forms on the website.'
        async_to_sync(bot.send_message)(chat_id, text)
        signature = message[1]
        user_id = signer.unsign(signature)
        TelegramUser.objects.update_or_create(user_id=user_id, chat=chat_id)
    else:
        return HttpResponse('Command is not recognized')
    return HttpResponse(update)
