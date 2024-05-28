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
        stock = types.KeyboardButton('Акции 💎')
        company = types.KeyboardButton('О компании ℹ️')
        free = types.KeyboardButton('Бесплатные линзы 🎁')
        notification = types.KeyboardButton('Напоминание ⏰')
        catalog = types.KeyboardButton('Каталог 🗂')
        delivery = types.KeyboardButton('Доставка 🚚')
        lenses = types.KeyboardButton('Памятка 💌')
        keyboard.add(stock, company, free, notification, catalog, delivery, lenses)
        return keyboard

    def admin_btns(self):
        one = types.InlineKeyboardButton('Экспорт БД 📨', callback_data='export')
        self.__markup.add(one)
        return self.__markup

    def registration_btns(self):
        reg = types.InlineKeyboardButton('Зарегестрироваться 👥', url='https://www.illusion-lens.ru/product/besplatnaya-para-linz-illusion-aero-light/?utm_source=tg&utm_medium=illusionbot')
        self.__markup.add(reg)
        return self.__markup

    def about_btns(self):
        magasine = types.InlineKeyboardButton('Интернет-магазин', url='https://www.illusion-lens.ru/?utm_source=tg&utm_medium=illusionbot')
        contact = types.InlineKeyboardButton('Контактные данные', callback_data='condata')
        self.__markup.add(magasine, contact)
        return self.__markup

    def actions_btns(self):
        free = types.InlineKeyboardButton('Бесплатные линзы', callback_data='freelenses')
        promo = types.InlineKeyboardButton('Промокод на первый заказ', callback_data='promokod')
        self.__markup.add(free, promo)
        return self.__markup

    def catalog_btns(self):
        color = types.InlineKeyboardButton('Цветные линзы', callback_data='switch1')
        transperent = types.InlineKeyboardButton('Остальные линзы', callback_data='switch2')
        uncolor = types.InlineKeyboardButton('Прозрачные линзы', callback_data='switch3')
        self.__markup.add(transperent, color, uncolor)
        return self.__markup

    def color_btns(self, colors):
        markup = types.InlineKeyboardMarkup(row_width=1)
        for color in colors:
            aero = types.InlineKeyboardButton(color[1], callback_data=f'color{color[0]}')
            markup.add(aero)
        return markup

    def switch_btns(self, links):
        company_names = {0: 'Wilberries', 1: 'Ozon', 2: 'Yandex Market'}
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('<', callback_data=f'card_switch2')
        btn2 = types.InlineKeyboardButton('>', callback_data=f'card_switch1')
        for index, link in enumerate(links):
            if link is not None:
                btn3 = types.InlineKeyboardButton(company_names[index], url=link)
                markup.add(btn3)
        btn4 = types.InlineKeyboardButton('Назад⤵️', callback_data='card_switch3')
        markup.add(btn1, btn2, btn4)
        return markup