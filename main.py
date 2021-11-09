from telegram.ext import Updater, CommandHandler, ConversationHandler, \
    CallbackQueryHandler, MessageHandler, Filters
from Conversation import *


def main():
    updater = Updater(token='', use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', get_fname)],
        states={
            'get_contact': [MessageHandler(Filters.text, get_contact)],
        },
        fallbacks=[CommandHandler('start', get_fname)]
    )
    dispatcher.add_handler(conv_handler)
    # dispatcher.add_handler(CallbackQueryHandler(inline_callback_region))
    # dispatcher.add_handler(CallbackQueryHandler(lesson_in))

    updater.start_polling()
    updater.idle()


main()
