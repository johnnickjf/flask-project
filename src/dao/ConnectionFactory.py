import os
import logging
import mysql.connector
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))


class ConnectionFactory:

    def __init__(self):
        self.__host = os.getenv('HOST')
        self.__user = os.getenv('USER')
        self.__password = os.getenv('PASSWORD')
        self.__database = os.getenv('DATABASE')
        self.__mydb = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password,
                                              database=self.__database)

    def insert(self, query, values):
        try:
            cursor = self.__mydb.cursor()
            cursor.execute(query, values)
            self.__mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def select(self, query, values):
        try:
            cursor = self.__mydb.cursor()
            cursor.execute(query, values)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def update(self, query, values):
        try:
            cursor = self.__mydb.cursor()
            cursor.execute(query, values)
            self.__mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def delete(self, query, values):
        try:
            cursor = self.__mydb.cursor()
            cursor.execute(query, values)
            self.__mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False
