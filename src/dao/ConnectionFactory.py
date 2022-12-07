from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))


class ConnectionFactory:

    def __init__(self, app):
        self.__app = app
        self.__app.config['MYSQL_HOST'] = os.getenv('HOST')
        self.__app.config['MYSQL_USER'] = os.getenv('USER')
        self.__app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORD')
        self.__app.config['MYSQL_DB'] = os.getenv('DATABASE')

    def connect(self):
        mysql = MySQL(self.__app)
        cursor = mysql.connection.cursor()
        return cursor


