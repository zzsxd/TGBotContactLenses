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

    def admin_btns(self):
        one = types.InlineKeyboardButton('Экспорт БД', callback_data='export')
        self.__markup.add(one)
        return self.__markup

    def registration_btns(self):
        reg = types.InlineKeyboardButton('Зарегестрироваться!', url='https://www.illusion-lens.ru/product/besplatnaya-para-linz-illusion-aero-light/')
        self.__markup.add(reg)
        return self.__markup

    def about_btns(self):
        magasine = types.InlineKeyboardButton('Интернет-магазин', url='illusion-lens.ru')
        contact = types.InlineKeyboardButton('Контактные данные', callback_data='condata')
        self.__markup.add(magasine, contact)
        return self.__markup


    def catalog_btns(self):
        transparent = types.InlineKeyboardButton('Прозрачные линзы', callback_data='transparent')
        blue = types.InlineKeyboardButton('Голубые линзы', callback_data='blue')
        green = types.InlineKeyboardButton('Зеленые линзы', callback_data='green')
        gray = types.InlineKeyboardButton('Серые линзы', callback_data='gray')
        black = types.InlineKeyboardButton('Черные линзы', callback_data='black')
        brown = types.InlineKeyboardButton('Карие линзы', callback_data='brown')
        violet = types.InlineKeyboardButton('Фиолетовые линзы', callback_data='violet')
        carnaval = types.InlineKeyboardButton('Карнавальные линзы', callback_data='carnaval')
        solutions = types.InlineKeyboardButton('Растворы и аксессуары', callback_data='solutions')
        self.__markup.add(transparent, blue, green, gray, black, brown, violet, carnaval, solutions)
        return self.__markup

    def transparent_btns(self):
        aero = types.InlineKeyboardButton('Illusion Aero', callback_data="aero")
        aero_light = types.InlineKeyboardButton('Illusion Aero Light', callback_data="light")
        test_illusion = types.InlineKeyboardButton('Тестовый набор Illusion', callback_data="test")
        clear = types.InlineKeyboardButton('Illusion Clear (4 блистера)', callback_data='clear')
        clear2 = types.InlineKeyboardButton('Illusion Clear (2 блистера)', callback_data='clear2')
        fashion = types.InlineKeyboardButton('Illusion Fashion', callback_data='fashion')
        self.__markup.add(aero, aero_light, test_illusion, clear, clear2, fashion)
        return self.__markup

    def blue_lenses_btns(self):
        glowblue = types.InlineKeyboardButton('Illusion Colors Glow', callback_data='glowblue')
        eleganceblue = types.InlineKeyboardButton('Illusion Colors Elegance', callback_data='eleganceblue')
        geodiamondblue = types.InlineKeyboardButton('Illusion Geo Diamond', callback_data='geodiamondblue')
        geomagicblue = types.InlineKeyboardButton('Illusion Geo Magic', callback_data='geomagicblue')
        geonatureblue = types.InlineKeyboardButton('Illusion Geo Nature', callback_data='geonatureblue')
        luxeblue = types.InlineKeyboardButton('Illusion Luxe', callback_data='luxeblue')
        shineblue = types.InlineKeyboardButton('Illusion Shine', callback_data='shineblue')
        fashionadonisblue = types.InlineKeyboardButton('Illusion Fashion Adonis', callback_data='fashionadonisblue')
        self.__markup.add(glowblue, eleganceblue, geodiamondblue, geomagicblue, geonatureblue, luxeblue, shineblue, fashionadonisblue)
        return self.__markup

    def green_lenses_btns(self):
        glowgreen = types.InlineKeyboardButton('Illusion Colors Glow', callback_data='glowgreen')
        elegancegreen = types.InlineKeyboardButton('Illusion Colors Elegance', callback_data='elegancegreen')
        geodiamondgreen = types.InlineKeyboardButton('Illusion Geo Diamond', callback_data='geodiamondgreen')
        geomagicgreen = types.InlineKeyboardButton('Illusion Geo Magic', callback_data='geomagicgreen')
        geonaturegreen = types.InlineKeyboardButton('Illusion Geo Nature', callback_data='geonaturegreen')
        luxegreen = types.InlineKeyboardButton('Illusion Luxe', callback_data='luxegreen')
        shinegreen = types.InlineKeyboardButton('Illusion Shine', callback_data='shinegreen')
        fashionadonisgreen = types.InlineKeyboardButton('Illusion Fashion Adonis', callback_data='fashionadonisgreen')
        fashionluxegreen = types.InlineKeyboardButton('Illusion Fashion Luxe', callback_data='fashionluxegreen')
        self.__markup.add(glowgreen, elegancegreen, geodiamondgreen, geomagicgreen, geonaturegreen, luxegreen, shinegreen, fashionadonisgreen, fashionluxegreen)
        return self.__markup

    def gray_lenses_btns(self):
        glowgray = types.InlineKeyboardButton('Illusion Colors Glow', callback_data='glowgray')
        elegancegray = types.InlineKeyboardButton('Illusion Colors Elegance', callback_data='elegancegray')
        colorshinegray = types.InlineKeyboardButton('Illusion Colors Shine', callback_data='geodiamondgray')
        geomagicgray = types.InlineKeyboardButton('Illusion Geo Magic', callback_data='geomagicgray')
        geonaturegray = types.InlineKeyboardButton('Illusion Diamond', callback_data='geonaturegray')
        adonisgray = types.InlineKeyboardButton('Illusion Fashion Adonis', callback_data='luxegray')
        luxegray = types.InlineKeyboardButton('Illusion Fashion Luxe', callback_data='shinegray')
        self.__markup.add(glowgray, elegancegray, colorshinegray, geomagicgray, geonaturegray, adonisgray, luxegray)
        return self.__markup

    def black_lenses_btns(self):
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        colorshineblack = types.InlineKeyboardButton('Illusion Colors Shine', callback_data='colorshineblack')
        adonisblack = types.InlineKeyboardButton('Illusion Fashion Adonis', callback_data='fashionadonisblack')
        self.__markup.add(glowblack, colorshineblack, adonisblack)
        return self.__markup

    def brown_lenses_btns(self):
        elegancebrown = types.InlineKeyboardButton('Illusion Colors Elegance', callback_data='elegancebrown')
        colorshinebrown = types.InlineKeyboardButton('Illusion Colors Shine', callback_data='colorshinebrown')
        geodiamondbrown = types.InlineKeyboardButton('Illusion Geo Diamond', callback_data='geodiamondbrown')
        adonisbrown = types.InlineKeyboardButton('Illusion Fashion Adonis', callback_data='luxebrown')
        luxebrown = types.InlineKeyboardButton('Illusion Fashion Luxe', callback_data='shinebrown')
        self.__markup.add(elegancebrown, colorshinebrown, geodiamondbrown, adonisbrown, luxebrown)
        return self.__markup

    def violet_lenses_btns(self):
        eleganceviolet = types.InlineKeyboardButton('Illusion Colors Elegance', callback_data='eleganceviolet')
        colorshineviolet = types.InlineKeyboardButton('Illusion Colors Shine', callback_data='colorshineviolet')
        adonisviolet = types.InlineKeyboardButton('Illusion Fashion Adonis', callback_data='luxeviolet')
        luxeviolet = types.InlineKeyboardButton('Illusion Fashion Luxe', callback_data='shineviolet')
        self.__markup.add(eleganceviolet, colorshineviolet, adonisviolet, luxeviolet)
        return self.__markup

    def carnaval_lenses_btns(self):
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', callback_data='colorsrioblack')
