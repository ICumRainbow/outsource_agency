import os

from django.conf import settings
from telegram.ext import ApplicationBuilder

TOKEN = settings.TELEGRAM['TOKEN']

PORT = int(os.environ.get('PORT', '8443'))
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# logger = logging.getLogger(__name__)
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     requests.post(
#         url='a835-213-230-80-188.eu.ngrok.io/contact_outsource_bot/' + TOKEN,
#         json=update.to_json())
#     await context.bot.send_message(chat_id=update.effective_chat.id, text='TEST', parse_mode=ParseMode.HTML)
#
#
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()  # this code creates our application using token of our bot
    # handlers = [  # setting handlers for our bot
    #     CommandHandler('start', start),
    # ]
    # application.add_handlers(handlers)  # adding handlers
    application.run_webhook(  # adding webhooks only if the bot is run on a hosting
        listen="127.0.0.1",
        port=PORT,
        url_path=TOKEN,
        webhook_url='koodrick.com/contact_outsource_bot/' + TOKEN,
    )
    # application.run_polling()  # we use polling in case we want to test it by running it on our PC
