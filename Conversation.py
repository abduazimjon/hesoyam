from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
# from Registratsiya import *
from keyboards import *


def get_fname(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Assalom alaykum, hurmatli foydalanuvchi, iltimos ro\'yxatdan o\'ting! '
                                  '\nIsm familiyangizni kiriting:')
    return 'get_contact'


def get_contact(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f'{message}! \nIltimos, nomerni ulashish tugmasini bosing',
                             reply_markup=contact())
    return 'main'


def contact():
    con_keyboard = KeyboardButton(text="Nomerni ulashish", request_contact=True)
    custom_keyboard = [[con_keyboard]]
    return ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True, one_time_keyboard=True)


def inline_callback_region():
    regions = get_region()
    region = []
    t = []
    for x in regions:
        t.append(InlineKeyboardButton(f'{x[1]}', callback_data=f'{x[0]}'))
        if len(t) == 2:
            region.append(t)
            t = []
        elif len(regions) - len(region) == 7:
            region.append(t)
            t = []
    return InlineKeyboardMarkup(region)
