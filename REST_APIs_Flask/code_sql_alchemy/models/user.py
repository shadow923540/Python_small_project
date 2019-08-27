import sqlite3

class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) #Parametry musza byc w formie tuple,
        #a zeby uzyc 1 argumentowego tuple trzeba z przecinkiem
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user= None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,)) #Parametry musza byc w formie tuple
        row = result.fetchone()
        if row:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user= None

        connection.close()
        return user