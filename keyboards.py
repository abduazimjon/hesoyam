from telegram import InlineKeyboardButton, InlineKeyboardMarkup, replymarkup, keyboardbutton, KeyboardButton, \
    ReplyKeyboardMarkup
from ConnectDB import *


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
