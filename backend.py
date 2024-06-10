#####################################
#            Created by             #
#               zzsxd               #
#####################################
import os
import time
import pandas as pd
import csv
from openpyxl import load_workbook

#####################################


class TempUserData:
    def __init__(self):
        super(TempUserData, self).__init__()
        self.__user_data = {}

    def temp_data(self, user_id):
        if user_id not in self.__user_data.keys():
            self.__user_data.update({user_id: [None, None, [], []]})
        return self.__user_data


class DbAct:
    def __init__(self, db, config, path_xlsx):
        super(DbAct, self).__init__()
        self.__db = db
        self.__config = config
        self.__fields = ['Имя', 'Фамилия', 'Никнейм']
        self.__dump_path_xlsx = path_xlsx

    def add_user(self, user_id, first_name, last_name, nick_name):
        if not self.user_is_existed(user_id):
            if user_id in self.__config.get_config()['admins']:
                is_admin = True
            else:
                is_admin = False
            self.__db.db_write(
                'INSERT INTO users (user_id, first_name, last_name, nick_name, is_admin) VALUES (?, ?, ?, ?, ?)',
                (user_id, first_name, last_name, nick_name, is_admin))

    def user_is_existed(self, user_id):
        data = self.__db.db_read('SELECT count(*) FROM users WHERE user_id = ?', (user_id,))
        if len(data) > 0:
            if data[0][0] > 0:
                status = True
            else:
                status = False
            return status

    def user_is_admin(self, user_id):
        data = self.__db.db_read('SELECT is_admin FROM users WHERE user_id = ?', (user_id,))
        if len(data) > 0:
            if data[0][0] == 1:
                status = True
            else:
                status = False
            return status

    def get_categories_by_id(self, row_id, title):
        return self.__db.db_read('SELECT `photo`, `desc` FROM `categories` WHERE `row_id` = ? AND `type` = ?', (row_id, title))[0]

    def get_product_by_id(self, row_id):
        return self.__db.db_read('SELECT `photo`, `title`, `link`, `ozon`, `yamarket`, `illusion` FROM `products` WHERE `row_id` = ?', (row_id, ))[0]

    def carnaval_by_title(self, title):
        return self.__db.db_read('SELECT `photo`, `desc` FROM `categories` WHERE `type` = ?',
                                 (title, ))[0]

    def get_products_by_lifetime(self, lifetime, type):
        return self.__db.db_read('SELECT `row_id`, `title` FROM `products` WHERE `lifetime` = ? AND `type` = ?', (lifetime, type))

    def get_products_by_color(self, color, type):
        return self.__db.db_read('SELECT `row_id`, `title` FROM `products` WHERE `color` = ? AND `type` = ?', (color, type))

    def get_products_by_type(self, type):
        return self.__db.db_read('SELECT `row_id`, `title` FROM `products` WHERE `type` = ?',
                                 (type, ))

    def get_colors(self):
        return self.__db.db_read('SELECT `row_id`, `title` FROM `colors`', ())

    def db_export_xlsx(self):
        d = {'Имя': [], 'Фамилия': [], 'Никнейм': []}
        users = self.__db.db_read('SELECT first_name, last_name, nick_name FROM users', ())
        if len(users) > 0:
            for user in users:
                for info in range(len(list(user))):
                    d[self.__fields[info]].append(user[info])
            df = pd.DataFrame(d)
            df.to_excel(self.__config.get_config()['xlsx_path'], sheet_name='пользователи', index=False)
