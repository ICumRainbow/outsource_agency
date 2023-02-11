import logging
import os

from django.conf import settings
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes

TOKEN = settings.TELEGRAM['TOKEN']

PORT = int(os.environ.get('PORT', '8443'))
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # response = requests.post(
    #     url='https://8d1d-109-105-160-58.eu.ngrok.io/telegram/contact_outsource_bot/' + TOKEN,
    #     json=update.to_json())
    await context.bot.send_message(chat_id=update.effective_chat.id, text='TEST', parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()  # this code creates our application using token of our bot
    handlers = [  # setting handlers for our bot
        CommandHandler('start', start),
    ]
    application.add_handlers(handlers)  # adding handlers
    application.run_webhook(  # adding webhooks only if the bot is run on a hosting
        listen="127.0.0.1",
        port=PORT,
        url_path=TOKEN,
        webhook_url='https://a835-213-230-80-188.eu.ngrok.io/telegram/contact_outsource_bot/' + TOKEN,
    )
    # application.run_polling()  # we use polling in case we want to test it by running it on our PC
