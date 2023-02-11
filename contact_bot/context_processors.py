from django.core.signing import Signer

from .models import TelegramUser


class TelegramSigner(Signer):
    """
        Telegram does not allow ':' as value of start parameter, this wrapper makes Django Signer compatible with Telegram.
    """

    def sign(self, value):
        return super().sign(value).replace(':', '-')

    def unsign(self, signed_value):
        return super().unsign(signed_value.replace('-', ':', 1))


signer = TelegramSigner()


def get_telegram_link(request):
    signed = signer.sign(request.user.id)
    context = {
        'link': signed,
    }
    return context


def check_user_linked(request):
    user_linked = request.user.id in TelegramUser.objects.values_list('user_id', flat=True)
    return {'user_linked': user_linked}
