""" Module for users management. """

import pymysql  # import pymysql to connect to the database MySQL Python
# Import class configApp
from application.config_app import ConfigApp


class User():
    """
    Class for users management:
    save users in database MySQL,
    check if user is authorized,
    check if user is pending,
    list users,
    activate user, deactivate user,
    save messages of users in database MySQL,
    list messages of users.
    """

    def __init__(self):
        """
        constructor for class

        Initialize the connection to the database MySQL
        and save in variable conexion.
        Use class configApp for get the parameters of connection
        to the database MySQL.

        args:
        ----------
        self : object
            Object of class
        """
        mysql = ConfigApp()
        self.conn = pymysql.connect(host=mysql.MYSQL_HOST,
                                    user=mysql.MYSQL_USER,
                                    password=mysql.MYSQL_PASSWORD,
                                    database=mysql.MYSQL_DATABASE)
        config = ConfigApp()
        self.chatIdSoporte = config.CHAT_ID_SOPORTE

    def CheckUser(self, chatId):
        """
        method for check if user is saved in database MySQL

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user

        return:
        ----------
        rows : int
            Number of rows of the query
        """
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT id FROM users WHERE chatid = '+chatId
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        rows = len(self.result)
        return rows

    def SavedUser(self, chatId, first_name, username):
        """
        method for save user in database MySQL

        args:
        ----------
        self : object
            Object of class
        chatId : str

        first_name : str
            First name of user
        username : str
            Username of user
        """
        self.cursor = self.conn.cursor()
        self.sql = "INSERT INTO users (chatId, first_name, username) \
        VALUES ( %s, %s, %s)"
        result = (chatId, first_name, username)
        self.cursor.execute(self.sql, result)
        self.conn.commit()

    def ChekAuthorizedUser(self, chatId):
        """
        check if user is authorized

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user

        return:
        ----------
        rows : int
            Number of rows of the query
        """
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT id FROM users WHERE chatid = ' \
            + chatId+' and authorized = 1'
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        rows = len(self.result)
        return rows

    def RequestUser(self, chatId):
        """
        received request of user for use the bot
        update status pending in database MySQL

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user
        """
        self.cursor = self.conn.cursor()
        self.sql = "UPDATE users SET pending = 1 WHERE chatid = "+chatId
        self.cursor.execute(self.sql)
        self.conn.commit()

    def CheckRequestUser(self, chatId):
        """
        check if user is pending

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user

        return:
        ----------
        rows : int
            Number of rows of the query
        """
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT pending FROM users WHERE chatid = '+chatId+' \
            and pending = 1'
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        rows = len(self.result)
        return rows

    def ListUsers(self):
        """
        get all users of database MySQL
        and show in Bot

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the users of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT CONCAT (id, '-', chatid, '-', \
        first_name, '-', username) AS user \
            FROM users ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        list_users = list()
        for row in self.result:
            user = row[0]
            list_users.append(user)
        users = '\n'.join(list_users)
        return users

    def ListUsersWeb(self):
        self.cursor = self.conn.cursor()
        self.sql = "SELECT id, chatid, first_name, username, authorized, \
            pending FROM users ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        return self.result

    def ChatIdUsers(self):
        """
        get all chatId of users of database MySQL

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the chatId of users of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT chatid FROM users"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        return self.result

    def ActivateUserWeb(self, id):
        """
        activate user in database MySQL

        args:
        ----------
        self : object
            Object of class
        id : int
            Id of user
        """
        self.cursor = self.conn.cursor()
        self.sql = "UPDATE users SET authorized = 1,\
        pending = 0 WHERE id = "+id
        self.cursor.execute(self.sql)
        self.conn.commit()

    def DeactivateUserWeb(self, id):
        """
        deactivate user in database MySQL

        args:
        ----------
        self : object
            Object of class
        id : int
            Id of user
        """
        self.cursor = self.conn.cursor()
        self.sql = "UPDATE users SET authorized = 0, \
            pending = 1 WHERE id = "+id
        self.cursor.execute(self.sql)
        self.conn.commit()

    def ListUsersPending(self):
        """
        get all users pending of database MySQL

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the users pending of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name, '-', \
            username) AS user FROM users \
                WHERE pending = 1 ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        list_users = list()
        for row in self.result:
            user = row[0]
            list_users.append(user)
        users = '\n'.join(list_users)
        return users

    def ListAuthorizedUsers(self):
        """
        get all users authorized of database MySQL

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the users authorized of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT CONCAT (id, '-', chatid, '-',first_name, '-', \
            username) AS user FROM users \
                WHERE authorized = 1 ORDER BY id DESC"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        list_users = list()
        for row in self.result:
            user = row[0]
            list_users.append(user)
        users = '\n'.join(list_users)
        return users

    def SavedMessageUser(self, chatId, first_name, text, username):
        """
        save message of user in database MySQL

        args:
        ----------
        self : object
            Object of class
        chatId : str
        first_name : str
            First name of user
        text : str
            Text of message
        username : str
            Username of user
        """
        self.cursor = self.conn.cursor()
        self.sql = "INSERT INTO messages (chatId, first_name, message, \
            username) VALUES ( %s, %s, %s, %s)"
        result = (chatId, first_name, text, username)
        self.cursor.execute(self.sql, result)
        self.conn.commit()

    def ListMessagesWeb(self):
        """
        get all messages of users of database MySQL
        limit 100 messages

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the messages of users of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT updated, first_name, username, message \
            FROM messages ORDER BY updated DESC LIMIT 100"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        return self.result