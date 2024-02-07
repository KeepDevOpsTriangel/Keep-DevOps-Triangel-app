""" This module is used to manage the state of the application. """

import pymysql  # Import pymysql for use database MySQL with Python
# Import ConfigApp for use variables of environment
from application.config_app import ConfigApp


class StateApp():
    """
    Class for manage the state of the application

    Use MySQL Python to connect to the database MySQL
    and query the state of the application.
    Update the state of the application, 
    activate or deactivate the application.
    """

    def __init__(self):
        """
        constructor for class

        Initialize the connection to the database MySQL
        """
        mysql = ConfigApp()
        self.conn = pymysql.connect(host=mysql.MYSQL_HOST,
                                    user=mysql.MYSQL_USER,
                                    password=mysql.MYSQL_PASSWORD,
                                    database=mysql.MYSQL_DATABASE)

    def CheckState(self):
        """
        check the state of the application

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        state : int
            State of the application
        """
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT state FROM state WHERE id = 1'
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        for row in self.result:
            state = row[0]
            return state

    def CheckStateWeb(self):
        """
        check the state of the application for web

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        state : int
            State of the application
        """
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT state FROM state WHERE id = 1'
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        for row in self.result:
            state = row[0]
            return state

    def GetNoteState(self):
        """
        obtain the notes of the state of the application
        for send to user in Telegram Bot

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        note : str
            Notes of the state of the application
        """
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT note FROM state WHERE id = 1'
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        for row in self.result:
            note = row[0]
            return note

    def UpdateNoteState(self, note):
        """
        update the notes of the state of the application
        to show to user in Telegram Bot

        args:
        ----------
        self : object
            Object of class
        note : str
        """
        self.cursor = self.conn.cursor()
        self.sql = 'UPDATE state SET note = "'+note+'" WHERE id = 1'
        self.cursor.execute(self.sql)
        self.conn.commit()

    def ActivateState(self):
        """
        activate the state of the application

        args:
        ----------
        self : object
            Object of class
        """
        self.cursor = self.conn.cursor()
        self.sql = 'UPDATE state SET state = 1 WHERE id = 1'
        self.cursor.execute(self.sql)
        self.conn.commit()

    def DeactivateState(self):
        """
        deactivate the state of the application

        args:
        ----------
        self : object
            Object of class
        """
        self.cursor = self.conn.cursor()
        self.sql = 'UPDATE state SET state = 0 WHERE id = 1'
        self.cursor.execute(self.sql)
        self.conn.commit()
