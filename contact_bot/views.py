import json
from pprint import pprint

import telegram
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from contact_bot.context_processors import TelegramSigner
from contact_bot.models import TelegramUser

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


class TelegramBotView(View):
    update = None

    def post(self, request, *args, **kwargs):
        token = kwargs.get('token')
        self.update: telegram.Update = parse_update(bot, request_token=token, request=request)
        return HttpResponse(self.update)


signer = TelegramSigner()


@csrf_exempt
def telegram_view(request, token):
    # signer.unsign(signature)
    update: telegram.Update = parse_update(bot, request_token=token, request=request)
    update_json = json.loads(update.to_json())
    signature = update_json['message']['text'].split()[1]
    chat_id = update_json['message']['chat']['id']
    user_id = signer.unsign(signature)
    TelegramUser.objects.update_or_create(user_id=user_id, chat=chat_id)
    return HttpResponse(update)
