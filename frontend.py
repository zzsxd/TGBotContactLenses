#####################################
#            Created by             #
#               zzsxd               #
#####################################
import telebot
from telebot import types


#####################################

class Bot_inline_btns:
    def __init__(self):
        super(Bot_inline_btns, self).__init__()
        self.__markup = types.InlineKeyboardMarkup(row_width=1)

    def start_btns(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        stock = types.KeyboardButton('Все акции')
        company = types.KeyboardButton('О компании')
        free = types.KeyboardButton('Бесплатные линзы')
        notification = types.KeyboardButton('Напоминание')
        catalog = types.KeyboardButton('Каталог')
        keyboard.add(stock, company, free, notification, catalog)
        return keyboard