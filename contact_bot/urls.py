from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import telegram_view

urlpatterns = [
    # path('bot/<str:token>/<str:signature>', csrf_exempt(TelegramBotView.as_view()), name='telegram_bot'),
    path('contact_outsource_bot/<str:token>', telegram_view, name='telegram'),
]