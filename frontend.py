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

    def pre_start_btns(self):
        contact = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contact = types.KeyboardButton('Поделиться контактом', request_contact=True)

    def start_btns(self):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        stock = types.KeyboardButton('Акции')
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

    def actions_btns(self):
        free = types.InlineKeyboardButton('Бесплатные линзы', callback_data='freelenses')
        self.__markup.add(free)
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
        aero = types.InlineKeyboardButton('Illusion Aero', url='https://www.illusion-lens.ru/product/illusion-aero/')
        aero_light = types.InlineKeyboardButton('Illusion Aero Light', url='https://www.illusion-lens.ru/product/illusion-aero-light/')
        test_illusion = types.InlineKeyboardButton('Тестовый набор Illusion', url='https://www.illusion-lens.ru/product/testovyj-nabor')
        clear = types.InlineKeyboardButton('Illusion Clear (4 блистера)', url='https://www.illusion-lens.ru/product/illusion-clear-2/')
        clear2 = types.InlineKeyboardButton('Illusion Clear (2 блистера)', url='https://www.illusion-lens.ru/product/illusion-clear/')
        fashion = types.InlineKeyboardButton('Illusion Fashion', url='https://www.illusion-lens.ru/product/illusion-fashion/')
        self.__markup.add(aero, aero_light, test_illusion, clear, clear2, fashion)
        return self.__markup

    def blue_lenses_btns(self):
        glowblue = types.InlineKeyboardButton('Illusion Colors Glow', url='https://www.illusion-lens.ru/product/illusion-colors-glow/')
        shineblue = types.InlineKeyboardButton('Illusion Colors Shine', url='https://www.illusion-lens.ru/product/illusion-colors-shine/')
        eleganceblue = types.InlineKeyboardButton('Illusion Colors Elegance', url='https://www.illusion-lens.ru/product/illusion-colors-elegance/')
        geodiamondblue = types.InlineKeyboardButton('Illusion Geo Diamond', url='https://www.illusion-lens.ru/product/illusion-geo-diamond/')
        geomagicblue = types.InlineKeyboardButton('Illusion Geo Magic', url='https://www.illusion-lens.ru/product/illusion-geo-magic/')
        geonatureblue = types.InlineKeyboardButton('Illusion Geo Nature', url='https://www.illusion-lens.ru/product/illusion-geo-nature/')
        luxeblue = types.InlineKeyboardButton('Illusion Fashion Luxe', url='https://www.illusion-lens.ru/product/illusion-fashion-luxe/')
        fashionadonisblue = types.InlineKeyboardButton('Illusion Fashion Adonis', url='https://www.illusion-lens.ru/product/illusion-fashion-adonis/')
        self.__markup.add(glowblue, eleganceblue, geodiamondblue, geomagicblue, geonatureblue, luxeblue, shineblue, fashionadonisblue)
        return self.__markup

    def green_lenses_btns(self):
        glowgreen = types.InlineKeyboardButton('Illusion Colors Glow', url='https://www.illusion-lens.ru/product/illusion-colors-glow/')
        shinegreen = types.InlineKeyboardButton('Illusion Colors Shine',
                                                url='https://www.illusion-lens.ru/illusion-colors-shine/')
        elegancegreen = types.InlineKeyboardButton('Illusion Colors Elegance', url='https://www.illusion-lens.ru/illusion-colors-elegance/')
        geodiamondgreen = types.InlineKeyboardButton('Illusion Geo Diamond', url='https://www.illusion-lens.ru/product/illusion-geo-diamond/')
        geomagicgreen = types.InlineKeyboardButton('Illusion Geo Magic', url='https://www.illusion-lens.ru/illusion-geo-magic/')
        geonaturegreen = types.InlineKeyboardButton('Illusion Geo Nature', url='https://www.illusion-lens.ru/product/illusion-geo-nature/')
        luxegreen = types.InlineKeyboardButton('Illusion Fashion Luxe', url='https://www.illusion-lens.ru/product/illusion-fashion-luxe/')
        fashionadonisgreen = types.InlineKeyboardButton('Illusion Fashion Adonis', url='https://www.illusion-lens.ru/product/illusion-fashion-adonis/')
        fashionluxegreen = types.InlineKeyboardButton('Illusion Fashion Luxe', url='https://www.illusion-lens.ru/product/illusion-fashion-luxe/')
        self.__markup.add(glowgreen, elegancegreen, geodiamondgreen, geomagicgreen, geonaturegreen, luxegreen, shinegreen, fashionadonisgreen, fashionluxegreen)
        return self.__markup

    def gray_lenses_btns(self):
        glowgray = types.InlineKeyboardButton('Illusion Colors Glow', url='https://www.illusion-lens.ru/product/illusion-colors-glow/')
        elegancegray = types.InlineKeyboardButton('Illusion Colors Elegance', url='https://www.illusion-lens.ru/product/illusion-colors-elegance/')
        colorshinegray = types.InlineKeyboardButton('Illusion Colors Shine', url='https://www.illusion-lens.ru/product/illusion-colors-shine/')
        geomagicgray = types.InlineKeyboardButton('Illusion Geo Magic', url='https://www.illusion-lens.ru/product/illusion-geo-magic/')
        geonaturegray = types.InlineKeyboardButton('Illusion Geo Diamond', url='https://www.illusion-lens.ru/product/illusion-geo-diamond/')
        adonisgray = types.InlineKeyboardButton('Illusion Fashion Adonis', url='https://www.illusion-lens.ru/product/illusion-fashion-adonis/')
        luxegray = types.InlineKeyboardButton('Illusion Fashion Luxe', url='https://www.illusion-lens.ru/product/illusion-fashion-luxe/')
        self.__markup.add(glowgray, elegancegray, colorshinegray, geomagicgray, geonaturegray, adonisgray, luxegray)
        return self.__markup

    def black_lenses_btns(self):
        glowblack = types.InlineKeyboardButton('Illusion Colors Rio', url='https://www.illusion-lens.ru/product/illusion-colors-rio-02/')
        colorshineblack = types.InlineKeyboardButton('Illusion Colors Shine', url='https://www.illusion-lens.ru/product/illusion-colors-shine/')
        adonisblack = types.InlineKeyboardButton('Illusion Fashion Adonis', url='https://www.illusion-lens.ru/product/illusion-colors-rio-02/')
        self.__markup.add(glowblack, colorshineblack, adonisblack)
        return self.__markup

    def brown_lenses_btns(self):
        elegancebrown = types.InlineKeyboardButton('Illusion Colors Elegance', url='https://www.illusion-lens.ru/product/illusion-colors-elegance/')
        colorshinebrown = types.InlineKeyboardButton('Illusion Colors Shine', url='https://www.illusion-lens.ru/product/illusion-colors-shine/')
        geodiamondbrown = types.InlineKeyboardButton('Illusion Geo Diamond', url='https://www.illusion-lens.ru/product/illusion-diamond-brown/')
        adonisbrown = types.InlineKeyboardButton('Illusion Fashion Adonis', url='https://www.illusion-lens.ru/product/illusion-fashion-adonis/')
        luxebrown = types.InlineKeyboardButton('Illusion Fashion Luxe', url='https://www.illusion-lens.ru/product/illusion-fashion-luxe/')
        self.__markup.add(elegancebrown, colorshinebrown, geodiamondbrown, adonisbrown, luxebrown)
        return self.__markup

    def violet_lenses_btns(self):
        eleganceviolet = types.InlineKeyboardButton('Illusion Colors Elegance', url='https://www.illusion-lens.ru/product/illusion-colors-shine/')
        colorshineviolet = types.InlineKeyboardButton('Illusion Colors Shine', url='https://www.illusion-lens.ru/product/illusion-colors-shine/')
        adonisviolet = types.InlineKeyboardButton('Illusion Fashion Adonis', url='https://www.illusion-lens.ru/product/illusion-fashion-adonis/')
        luxeviolet = types.InlineKeyboardButton('Illusion Fashion Luxe', url='https://www.illusion-lens.ru/product/illusion-fashion-luxe/')
        self.__markup.add(eleganceviolet, colorshineviolet, adonisviolet, luxeviolet)
        return self.__markup

    def carnaval_lenses_btns(self):
        carnaval1 = types.InlineKeyboardButton('Illusion Colors Rio 1', url='https://www.illusion-lens.ru/product/illusion-colors-rio-01/')
        carnaval2 = types.InlineKeyboardButton('Illusion Colors Rio 2', url='https://www.illusion-lens.ru/product/illusion-colors-rio-02/')
        carnaval3 = types.InlineKeyboardButton('Illusion Colors Rio 3', url='https://www.illusion-lens.ru/product/illusion-colors-rio-03/')
        carnaval4 = types.InlineKeyboardButton('Illusion Colors Rio 4', url='https://www.illusion-lens.ru/product/illusion-colors-rio-04/')
        carnaval5 = types.InlineKeyboardButton('Illusion Colors Rio 5', url='https://www.illusion-lens.ru/product/illusion-colors-rio-05/')
        carnaval6 = types.InlineKeyboardButton('Illusion Colors Rio 6', url='https://www.illusion-lens.ru/product/illusion-colors-rio-06/')
        carnaval7 = types.InlineKeyboardButton('Illusion Colors Rio 8', url='https://www.illusion-lens.ru/product/illusion-colors-rio-08/')
        carnaval8 = types.InlineKeyboardButton('Illusion Colors Rio 9', url='https://www.illusion-lens.ru/product/illusion-colors-rio-09/')
        carnaval9 = types.InlineKeyboardButton('Illusion Colors Rio 10', url='https://www.illusion-lens.ru/product/illusion-colors-rio-10/')
        carnaval10 = types.InlineKeyboardButton('Illusion Colors Rio 11', url='https://www.illusion-lens.ru/product/illusion-colors-rio-11/')
        carnaval11 = types.InlineKeyboardButton('Illusion Colors Rio 12', url='https://www.illusion-lens.ru/product/illusion-colors-rio-12/')
        carnaval12 = types.InlineKeyboardButton('Illusion Colors Rio 13', url='https://www.illusion-lens.ru/product/illusion-colors-rio-13/')
        carnaval13 = types.InlineKeyboardButton('Illusion Colors Rio 15', url='https://www.illusion-lens.ru/product/illusion-colors-rio-13/')
        carnaval14 = types.InlineKeyboardButton('Illusion Colors Rio 16', url='https://www.illusion-lens.ru/product/illusion-colors-rio-16/')
        carnaval15 = types.InlineKeyboardButton('Illusion Colors Rio 17', url='https://www.illusion-lens.ru/product/illusion-colors-rio-17/')
        carnaval16 = types.InlineKeyboardButton('Illusion Colors Rio 18', url='https://www.illusion-lens.ru/product/illusion-colors-rio-18/')
        carnaval17 = types.InlineKeyboardButton('Illusion Colors Rio 21', url='https://www.illusion-lens.ru/product/illusion-colors-rio-21/')
        carnaval18 = types.InlineKeyboardButton('Illusion Colors Rio 22', url='https://www.illusion-lens.ru/product/illusion-colors-rio-22/')
        carnaval19 = types.InlineKeyboardButton('Illusion Colors Rio 26', url='https://www.illusion-lens.ru/product/illusion-colors-rio-26/')
        carnaval20 = types.InlineKeyboardButton('Illusion Colors Rio 27', url='https://www.illusion-lens.ru/product/illusion-colors-rio-27/')
        carnaval21 = types.InlineKeyboardButton('Illusion Colors Rio 32', url='https://www.illusion-lens.ru/product/illusion-colors-rio-32/')
        carnaval22 = types.InlineKeyboardButton('Illusion Colors Rio 35', url='https://www.illusion-lens.ru/product/illusion-colors-rio-35/')
        carnaval23 = types.InlineKeyboardButton('Illusion Colors Rio 42', url='https://www.illusion-lens.ru/product/illusion-colors-rio-42/')
        carnaval24 = types.InlineKeyboardButton('Illusion Colors Rio 43', url='https://www.illusion-lens.ru/product/illusion-colors-rio-43/')
        carnaval25 = types.InlineKeyboardButton('Illusion Colors Rio 44', url='https://www.illusion-lens.ru/product/illusion-colors-rio-44/')
        carnaval26 = types.InlineKeyboardButton('Illusion Colors Rio 45', url='https://www.illusion-lens.ru/product/illusion-colors-rio-45/')
        carnaval27 = types.InlineKeyboardButton('Illusion Colors Rio 46', url='https://www.illusion-lens.ru/product/illusion-colors-rio-46/')
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
        stan = types.InlineKeyboardButton('Стандартный набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-4/')
        white = types.InlineKeyboardButton('Белый набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-5/')
        blue = types.InlineKeyboardButton('Голубой набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz/')
        yellow = types.InlineKeyboardButton('Желтый набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-2/')
        pink = types.InlineKeyboardButton('Розовый набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-3/')
        gray = types.InlineKeyboardButton('Серый набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-4/')
        silver = types.InlineKeyboardButton('Серебристый набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-serebristyj/')
        bluezerkal = types.InlineKeyboardButton('Голубой зеркальный набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-6/')
        turquoise = types.InlineKeyboardButton('Бирюзовый зеркальный набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-biryuzovyj-zerkalnyj/')
        silverzekral = types.InlineKeyboardButton('Серебристый зеркальный набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-serebristyj-zerkalnyj/')
        black = types.InlineKeyboardButton('Черный зеркальный набор', url='https://www.illusion-lens.ru/product/nabor-dlya-linz-chernyj-zerkalnyj/')
        self.__markup.add(stan, white, blue, yellow, pink, gray, silver, bluezerkal, turquoise, silverzekral, black)
        return self.__markup

    def water_btns(self):
        max = types.InlineKeyboardButton('Универсальный раствор 250мл', url='https://www.illusion-lens.ru/product/universalnyj-rastvor-dlya-kontaktnyh-linz-250-ml/')
        mini = types.InlineKeyboardButton('Универсальный раствор 125мл', url='https://www.illusion-lens.ru/product/universalnyj-rastvor-dlya-kontaktnyh-linz-125-ml/')
        self.__markup.add(max, mini)
        return self.__markup

    def drops_btns(self):
        stan = types.InlineKeyboardButton('Увлажняющие капли 10мл', url='https://www.illusion-lens.ru/product/uvlazhnyayushhie-kapli-illusion-10ml/')
        self.__markup.add(stan)
        return self.__markup

