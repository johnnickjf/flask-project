import os
import logging
import mysql.connector
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv('.env'))


class ConnectionFactory:

    def __init__(self):
        self.host = os.getenv('HOST')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.database = os.getenv('DATABASE')
        self.mydb = mysql.connector.connect(host=self.host, user=self.user, password=self.password,
                                            database=self.database)

    def insert(self, data):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(data['query'], data['values'])
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def select(self, data):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(data['query'], data['values'])
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def update(self, data):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(data['query'], data['values'])
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False

    def delete(self, data):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(data['query'], data['values'])
            self.mydb.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            # logging.error(e)
            return False
