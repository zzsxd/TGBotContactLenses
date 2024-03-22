#####################################
#            Created by             #
#               zzsxd               #
#####################################
config_name = 'secrets.json'
#####################################
import os
import telebot
import platform
from config_parser import ConfigParser
from frontend import Bot_inline_btns


def main():
    @bot.message_handler(commands=['start', 'admin'])
    def start_msg(message):
        buttons = Bot_inline_btns()
        command = message.text.replace('/', '')
        if command =='start':
            bot.send_message(message.chat.id, 'Стартовое сообщение', reply_markup=buttons.start_btns())
        elif command =='admin':
            bot.send_message(message.chat.id, 'Админ панель')
    @bot.message_handler(content_types=['text'])
    def text_msg(message):
        buttons = Bot_inline_btns()
        if message.text == 'Все акции':
            bot.send_message(message.chat.id, 'Что-то про акции')
        elif message.text == 'О компании':
            bot.send_message(message.chat.id, 'Что-то про компанию')
        elif message.text == 'Бесплатные линзы':
            bot.send_message(message.chat.id, 'Что-то про бесплатные линзы')
        elif message.text == 'Напоминание':
            bot.send_message(message.chat.id, 'Что-то про напоминание')
        elif message.text == 'Каталог':
            bot.send_message(message.chat.id, 'Что-то про каталог')
    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
