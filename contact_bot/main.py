import logging
import os
import requests
from django.conf import settings
import telegram
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Updater, CommandHandler, ApplicationBuilder, ContextTypes

# from contact_bot.context_processors import TelegramSigner
PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '5959733238:AAFfrkaFYhDlCsEEKrFbemHG1zEVlxQEPOQ'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.post(
        url='https://1af0-87-254-141-92.eu.ngrok.io/telegram/contact_outsource_bot/' + TOKEN,
        params=update.to_json())
    print(response)
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
        webhook_url='https://1af0-87-254-141-92.eu.ngrok.io/telegram/contact_outsource_bot/' + TOKEN
    )
    # application.run_polling()  # we use polling in case we want to test it by running it on our PC
