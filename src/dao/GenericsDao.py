
class GenericsDao:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect('db\database.db')
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def insert(self, query, values):
        self.connect()
        self.cursor.execute(query, values)
        self.connection.commit()
        self.close()

    def select(self, query, values):
        self.connect()
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        self.close()
        return result

    def update(self, query, values):
        self.connect()
        self.cursor.execute(query, values)
        self.connection.commit()
        self.close()

    def delete(self, x, y):
        self.connect()
        self.cursor.execute(x, y)
        self.connection.commit()
        self.close()
