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
            bot.send_message(message.chat.id, 'ILLUSION контактные линзы нового поколения!', reply_markup=buttons.start_btns())
        elif command =='admin':
            bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы успешно вошли в Админ-Панель!', reply_markup=buttons.admin_btns())
    @bot.message_handler(content_types=['text'])
    def text_msg(message):
        buttons = Bot_inline_btns()
        if message.text == 'Все акции':
            bot.send_message(message.chat.id, 'Что-то про акции')
        elif message.text == 'О компании':
            bot.send_message(message.chat.id, 'ILLUSION контактные линзы нового поколения!\n'
                                                    '\n'
                                                    'С 2012 года компания «Вижен Трейд» является эксклюзивным дистрибьютером контактных линз бренда ILLUSION.\n'
                                                    '\n'
                                                    'Безопасные современные контактные линзы нового поколения ILLUSION представлены в различной цветовой гамме с разнообразным дизайном и востребованы в кабинетах контактной коррекции, интернет - магазинах, аптеках, оптиках и в фармацевтических компаниях.\n'
                                                    '\n', reply_markup=buttons.about_btns())
        elif message.text == 'Бесплатные линзы':
            bot.send_message(message.chat.id, 'Получи бесплатную пару линз ILLUSION Aero Light.\n'
                                              '\n'
                                              'Регистрируйся на сайте, добавь тестовую пару линз в корзину, дождись доставку и наслаждайся идеальным зрением!\n'
                                              '\n'
                                              'Двухнедельные линзы ILLUSION Aero Light сделаны из инновационного материала — тонкие и упругие, они практически не чувствуются на глазах.\n'
                                              '\n'
                                              'ILLUSION Aero Light – это силикон-гидрогелевые линзы с высокой кислородопроницаемостью и повышенным влагосодержанием. Асферический дизайн линзы обеспечивает чёткое зрение даже при низкой освещенности.\n'
                                              '\n'
                                              'Тестируй ILLUSION Aero Light бесплатно!', reply_markup=buttons.registration_btns())
        elif message.text == 'Напоминание':
            bot.send_message(message.chat.id, 'Что-то про напоминание')
        elif message.text == 'Каталог':
            bot.send_message(message.chat.id, 'Каталог', reply_markup=buttons.catalog_btns())


    @bot.callback_query_handler(func=lambda call:True)
    def callback(call):
        buttons = Bot_inline_btns()
        if call.data == 'transparent':
            bot.send_message(call.message.chat.id, 'Прозрачные линзы', reply_markup=buttons.transparent_btns())
        elif call.data == '':
            pass
        elif call.data == 'condata':
            bot.send_message(call.message.chat.id, 'Группа ВК: vk.com/illusion_lens\n\n'
                                                   'Электронный адрес: info@illusion-lens.ru\n\n'
                                                   'Телефон для заказа через сайт или каталог товаров: 8 (812) 326 32 21 (Whatsapp, Telegram, Viber)\n\n'
                                                   'Время работы колл-центра: 9:30-18:00 Пн-Пт')
    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
