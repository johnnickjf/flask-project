import mysql.connector
import os
import logging
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))


class ConnectionFactory:

    def __init__(self):
        self.__host = os.getenv('HOST')
        self.__user = os.getenv('USER')
        self.__password = os.getenv('PASSWORD')
        self.__database = os.getenv('DATABASE')
        self.__mydb = mysql.connector.connect(host=os.getenv('HOST'), user=os.getenv('USER'),
                                              password=os.getenv('PASSWORD'),
                                              database=os.getenv('DATABASE'))

    def connect(self):
        try:
            return self.__mydb.cursor()
        except Exception as e:
            # logging.error(e)
            return False

    def insert(self, query, values):
        try:
            cursor = self.connect()
            cursor.execute(query, values)
            cursor.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            # logging.error(e)
            return False

    def select(self, query, values):
        try:
            cursor = self.connect()
            cursor.execute(query, values)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            # logging.error(e)
            return False

    def update(self, query, values):
        try:
            cursor = self.connect()
            cursor.execute(query, values)
            cursor.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            # logging.error(e)
            return False

    def delete(self, query, values):
        try:
            cursor = self.connect()
            cursor.execute(query, values)
            cursor.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            # logging.error(e)
            return False
