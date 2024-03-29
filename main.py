#####################################
#            Created by             #
#               zzsxd               #
#####################################
config_name = 'secrets.json'
reminders = {}  # словарь для хранения напоминаний для каждого пользователя
#####################################
import os
import telebot
import platform
from datetime import datetime
import threading
from threading import Lock
import time
from config_parser import ConfigParser
from frontend import Bot_inline_btns
from backend import TempUserData, DbAct
from db import DB


def main():
    @bot.message_handler(commands=['start', 'admin'])
    def start_msg(message):
        name_user = message.from_user.first_name
        user_id = message.from_user.id
        buttons = Bot_inline_btns()
        command = message.text.replace('/', '')
        db_actions.add_user(user_id, message.from_user.first_name, message.from_user.last_name,
                            f'@{message.from_user.username}')
        if command == 'start':
            bot.send_message(message.chat.id, '«<b>ILLUSION Lens</b>» - контактные линзы нового поколения!',
                             reply_markup=buttons.start_btns(), parse_mode="HTML")
        elif db_actions.user_is_admin(user_id):
            if command == 'admin':
                bot.send_message(message.chat.id, f'{message.from_user.first_name}, вы успешно вошли в Админ-Панель ✅',
                                 reply_markup=buttons.admin_btns())

    @bot.message_handler(content_types=['text'])
    def text_msg(message):
        user_id = message.chat.id
        buttons = Bot_inline_btns()
        code = temp_user_data.temp_data(user_id)[user_id][0]
        if db_actions.user_is_existed(user_id):
            if message.text == 'Акции 💎':
                bot.send_message(message.chat.id, 'Наши акции 💎', reply_markup=buttons.actions_btns())
            elif message.text == 'О компании ℹ️':
                bot.send_video(message.chat.id, open(video, 'rb'), width=1920, height=1080, reply_markup=buttons.about_btns())
            elif message.text == 'Бесплатные линзы 🎁':
                bot.send_message(message.chat.id, 'Получи бесплатную пару линз «ILLUSION Aero Light»!\n\n'
                                                  'Регистрируйся на сайте, добавь тестовую пару линз в корзину, '
                                                  'дождись доставку и наслаждайся идеальным зрением!\n\n'
                                                  'Двухнедельные линзы «ILLUSION Aero Light сделаны из инновационного '
                                                  'материала — тонкие и упругие, они практически не чувствуются на '
                                                  'глазах.\n\n'
                                                  '«ILLUSION Aero Light» – это силикон-гидрогелевые линзы с высокой '
                                                  'кислородопроницаемостью и повышенным влагосодержанием. '
                                                  'Асферический дизайн линзы обеспечивает чёткое зрение даже при '
                                                  'низкой освещенности.\n\n'
                                                  'Тестируй «ILLUSION Aero Light» бесплатно!',
                                 reply_markup=buttons.registration_btns())
            elif message.text == 'Каталог 🗂':
                bot.send_message(message.chat.id, 'Наш ассортимент товаров 🗂', reply_markup=buttons.catalog_btns())
            elif message.text == 'Напоминание ⏰':
                bot.send_message(message.chat.id,
                                 'Вы можете поставить себе <b>напоминание</b>, чтобы не забыть купить новые линзы!\n\n'
                                 'Введите дату, тогда бот пришлет вам напоминание!\n\n<i>(Дата в формате: DD.MM.YYYY HH:MM (<u>16.03.24 16:00</u>)</i>', parse_mode="HTML")
                temp_user_data.temp_data(user_id)[user_id][0] = 0
            elif code == 0:
                if message.text and ' ' in message.text:
                    try:
                        remind_time = datetime.strptime(message.text, '%d.%m.%Y %H:%M')
                        if user_id not in reminders:
                            reminders[user_id] = []
                        reminders[user_id].append((message.text, remind_time))
                        bot.reply_to(message, f"Напоминание на <b>{remind_time.strftime('%d.%m.%Y %H:%M')}</b> сохранено ✅", parse_mode="HTML")
                    except ValueError:
                        bot.reply_to(message, "🚫Неверный формат 🚫\n\n"
                                              "Используйте '<b>DD.MM.YYYY HH:MM</b>'", parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, 'Введите /start для запуска бота')

    def check_reminders():
        while True:
            current_time = datetime.now()
            for chat_id, reminder_list in reminders.items():
                new_list = []
                for text, remind_time in reminder_list:
                    if current_time >= remind_time:
                        bot.send_message(chat_id, f"⏰ Напоминание ⏰\n\n"
                                                  f"<b>Купите линзы!</b>", parse_mode="HTML")
                    else:
                        new_list.append((text, remind_time))
                reminders[chat_id] = new_list
            # Проверяем каждую минуту
            time.sleep(60)

    reminder_thread = threading.Thread(target=check_reminders)
    reminder_thread.start()

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        buttons = Bot_inline_btns()
        if call.data == 'export':
            db_actions.db_export_xlsx()
            bot.send_document(call.message.chat.id, open(config.get_config()['xlsx_path'], 'rb'))
            os.remove(config.get_config()['xlsx_path'])
        elif call.data == 'condata':
            bot.send_message(call.message.chat.id, 'Группа ВК: vk.com/illusion_lens\n\n'
                                                   'YouTube: https://www.youtube.com/@illusionlens1530\n\n'
                                                   'Pinterest: https://ru.pinterest.com/illusionlens/\n\n'
                                                   'Электронный адрес: info@illusion-lens.ru\n\n'
                                                   'Телефон для заказа через сайт или каталог товаров: 8 (812) 326 32 21 (Whatsapp, Telegram, Viber)\n\n'
                                                   'Время работы колл-центра: 9:30-18:00 Пн-Пт')
        elif call.data == 'freelenses':
            bot.send_message(call.message.chat.id, 'Получи бесплатную пару линз ILLUSION Aero Light.\n'
                                                   '\n'
                                                   'Регистрируйся на сайте, добавь тестовую пару линз в корзину, '
                                                   'дождись доставку и наслаждайся идеальным зрением!\n'
                                                   '\n'
                                                   'Двухнедельные линзы "ILLUSION Aero Light" сделаны из '
                                                   'инновационного материала — тонкие и упругие, они практически не '
                                                   'чувствуются на глазах.\n'
                                                   '\n'
                                                   'ILLUSION Aero Light – это силикон-гидрогелевые линзы с высокой '
                                                   'кислородопроницаемостью и повышенным влагосодержанием. '
                                                   'Асферический дизайн линзы обеспечивает чёткое зрение даже при '
                                                   'низкой освещенности.\n'
                                                   '\n'
                                                   'Тестируй "ILLUSION Aero Light" бесплатно!',
                             reply_markup=buttons.registration_btns())
        elif call.data == 'transperent':
            bot.send_message(call.message.chat.id, 'Прозрачные линзы 👀', reply_markup=buttons.transperent_btns())
        elif call.data == 'color':
            bot.send_message(call.message.chat.id, 'Цветные линзы 😎', reply_markup=buttons.color_btns())

    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    work_dir = os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser(f'{work_dir}/{config_name}', os_type)
    temp_user_data = TempUserData()
    db = DB(config.get_config()['db_file_name'], Lock())
    db_actions = DbAct(db, config, config.get_config()['xlsx_path'])
    video = config.get_config()['video']
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
