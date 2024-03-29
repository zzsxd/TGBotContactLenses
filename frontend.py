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
        keyboard.add(stock, company, free, notification, catalog)
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
        self.__markup.add(free)
        return self.__markup

    def catalog_btns(self):
        transperent = types.InlineKeyboardButton('Прозрачные линзы', callback_data='transperent')
        color = types.InlineKeyboardButton('Цветные линзы', callback_data='color')
        self.__markup.add(transperent, color)
        return self.__markup

    def transperent_btns(self):
        aero = types.InlineKeyboardButton('Aero', url='https://www.illusion-lens.ru/aero/?utm_source=tg&utm_medium=illusionbot')
        clear = types.InlineKeyboardButton('Clear', url='https://www.illusion-lens.ru/clear/?utm_source=tg&utm_medium=illusionbot')
        fashion = types.InlineKeyboardButton('Fashion', url='https://www.illusion-lens.ru/fashion/?utm_source=tg&utm_medium=illusionbot')
        self.__markup.add(aero, clear, fashion)
        return self.__markup

    def color_btns(self):
        blue = types.InlineKeyboardButton('Голубые линзы', url='https://www.illusion-lens.ru/blue/?utm_source=tg&utm_medium=illusionbot')
        green = types.InlineKeyboardButton('Зеленые линзы', url='https://www.illusion-lens.ru/green/?utm_source=tg&utm_medium=illusionbot')
        gray = types.InlineKeyboardButton('Серые линзы', url='https://www.illusion-lens.ru/gray/?utm_source=tg&utm_medium=illusionbot')
        black = types.InlineKeyboardButton('Черные линзы', url='https://www.illusion-lens.ru/black/?utm_source=tg&utm_medium=illusionbot')
        brown = types.InlineKeyboardButton('Карие линзы', url='https://www.illusion-lens.ru/brown/?utm_source=tg&utm_medium=illusionbot')
        violet = types.InlineKeyboardButton('Фиолетовые линзы', url='https://www.illusion-lens.ru/violet/?utm_source=tg&utm_medium=illusionbot')
        carnaval = types.InlineKeyboardButton('Карнавальные линзы', url='https://www.illusion-lens.ru/carnival/?utm_source=tg&utm_medium=illusionbot')
        self.__markup.add(blue, green, gray, black, brown, violet, carnaval)
        return self.__markup

