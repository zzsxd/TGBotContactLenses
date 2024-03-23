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
        carnaval1 = types.InlineKeyboardButton('Illusion Colors Rio 1', callback_data='carnaval1')
        carnaval2 = types.InlineKeyboardButton('Illusion Colors Rio 2', callback_data='carnaval2')
        carnaval3 = types.InlineKeyboardButton('Illusion Colors Rio 3', callback_data='carnaval3')
        carnaval4 = types.InlineKeyboardButton('Illusion Colors Rio 4', callback_data='carnaval4')
        carnaval5 = types.InlineKeyboardButton('Illusion Colors Rio 5', callback_data='carnaval5')
        carnaval6 = types.InlineKeyboardButton('Illusion Colors Rio 6', callback_data='carnaval6')
        carnaval7 = types.InlineKeyboardButton('Illusion Colors Rio 8', callback_data='carnaval7')
        carnaval8 = types.InlineKeyboardButton('Illusion Colors Rio 9', callback_data='carnaval8')
        carnaval9 = types.InlineKeyboardButton('Illusion Colors Rio 10', callback_data='carnaval9')
        carnaval10 = types.InlineKeyboardButton('Illusion Colors Rio 11', callback_data='carnaval10')
        carnaval11 = types.InlineKeyboardButton('Illusion Colors Rio 12', callback_data='carnaval11')
        carnaval12 = types.InlineKeyboardButton('Illusion Colors Rio 13', callback_data='carnaval12')
        carnaval13 = types.InlineKeyboardButton('Illusion Colors Rio 15', callback_data='carnaval13')
        carnaval14 = types.InlineKeyboardButton('Illusion Colors Rio 16', callback_data='carnaval14')
        carnaval15 = types.InlineKeyboardButton('Illusion Colors Rio 17', callback_data='carnaval15')
        carnaval16 = types.InlineKeyboardButton('Illusion Colors Rio 18', callback_data='carnaval16')
        carnaval17 = types.InlineKeyboardButton('Illusion Colors Rio 21', callback_data='carnaval17')
        carnaval18 = types.InlineKeyboardButton('Illusion Colors Rio 22', callback_data='carnaval18')
        carnaval19 = types.InlineKeyboardButton('Illusion Colors Rio 26', callback_data='carnaval19')
        carnaval20 = types.InlineKeyboardButton('Illusion Colors Rio 27', callback_data='carnaval20')
        carnaval21 = types.InlineKeyboardButton('Illusion Colors Rio 32', callback_data='carnaval21')
        carnaval22 = types.InlineKeyboardButton('Illusion Colors Rio 35', callback_data='carnaval22')
        carnaval23 = types.InlineKeyboardButton('Illusion Colors Rio 42', callback_data='carnaval23')
        carnaval24 = types.InlineKeyboardButton('Illusion Colors Rio 43', callback_data='carnaval24')
        carnaval25 = types.InlineKeyboardButton('Illusion Colors Rio 44', callback_data='carnaval25')
        carnaval26 = types.InlineKeyboardButton('Illusion Colors Rio 45', callback_data='carnaval26')
        carnaval27 = types.InlineKeyboardButton('Illusion Colors Rio 46', callback_data='carnaval27')
        self.__markup = types.InlineKeyboardMarkup(row_width=2)
        self.__markup.add(carnaval1, carnaval2, carnaval3, carnaval4, carnaval5, carnaval6, carnaval7, carnaval8, carnaval9, carnaval10, carnaval11, carnaval12, carnaval13, carnaval14, carnaval15, carnaval16, carnaval17, carnaval18, carnaval19, carnaval20, carnaval21, carnaval22, carnaval23, carnaval24, carnaval25, carnaval26, carnaval27)
        return self.__markup

    def solutions_btns(self):
        sets = types.InlineKeyboardButton('Наборы для линз', callback_data='sets')
        water = types.InlineKeyboardButton('Растворы', callback_data='water')
        drops = types.InlineKeyboardButton('Капли', callback_data='drops')
        self.__markup.add(sets, water, drops)
        return self.__markup

    def sets_btns(self):
        white = types.InlineKeyboardButton('Стандартный набор', callback_data='stankit')
        blue = types.InlineKeyboardButton('Голубой набор', callback_data='bluekit')
        yellow = types.InlineKeyboardButton('Желтый набор', callback_data='yellowkit')
        pink = types.InlineKeyboardButton('Розовый набор', callback_data='pinkkit')
        gray = types.InlineKeyboardButton('Серый набор', callback_data='graykit')
        silver = types.InlineKeyboardButton('Серебристый набор', callback_data='silverkit')
        bluezerkal = types.InlineKeyboardButton('Голубой зеркальный набор', callback_data='bluezkit')
        turquoise = types.InlineKeyboardButton('Бирюзовый зеркальный набор', callback_data='turkit')
        silverzekral = types.InlineKeyboardButton('Серебристый зеркальный набор', callback_data='silverzkit')
        black = types.InlineKeyboardButton('Черный зеркальный набор', callback_data='blackkit')
        self.__markup.add(white, blue, yellow, pink, gray, silver, bluezerkal, turquoise, silverzekral, black)
        return self.__markup

    def water_btns(self):
        max = types.InlineKeyboardButton('Универсальный раствор 250мл', callback_data='maxwater')
        mini = types.InlineKeyboardButton('Универсальный раствор 125мл', callback_data='miniwater')
        self.__markup.add(max, mini)
        return self.__markup

    def drops_btns(self):
        stan = types.InlineKeyboardButton('Увлажняющие капли 10мл', callback_data='standrops')
        self.__markup.add(stan)
        return self.__markup
