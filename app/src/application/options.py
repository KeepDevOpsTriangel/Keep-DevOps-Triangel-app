""" Module Options class to manage the options
of the bot to send to the user """

import pymysql  # import pymysql to connect to the database MySQL Python
from application.config_app import ConfigApp  # Import class configApp


class Options():
    """
    Class for manage the options of the bot to send to the user

    Use MySQL Python to connect to the database MySQL
    and query options to send to the user.
    """

    def __init__(self):
        """
        Constructor for class

        Initialize the connection to the database MySQL
        and save in variable conn.
        Use class ConfigApp for get the parameters of connection
        to the database MySQL.
        """
        mysql = ConfigApp()
        self.conn = pymysql.connect(host=mysql.MYSQL_HOST,
                                    user=mysql.MYSQL_USER,
                                    password=mysql.MYSQL_PASSWORD,
                                    database=mysql.MYSQL_DATABASE)

    def SendOptions(self):
        """
        method for send options to user in keyboard of Telegram Bot
        Obtain the options of database MySQL and save in variable result.

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        keyboard : dict
            Dictionary with the options of database MySQL        
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT opt FROM options"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        # options = [["1", "2", "3", "4"]]
        keyboard = {
            "keyboard": self.result,
            "one_time_keyboard": True,
            "remove_keyboard": True,
            "resize_keyboard": True,
        }
        self.conn.commit()
        self.cursor.close()
        return keyboard

    def EditOptions(self, id, option, text):
        """
        update text of option in database MySQL
        for use to send to user in keyboard of Telegram Bot

        args:
        ----------
        self : object
            Object of class
        id : int
            Id of option
        opt : str
            Name of option
        text : str
            Text of option
        """
        self.cursor = self.conn.cursor()
        self.sql = "UPDATE options SET opt = %s, text = %s WHERE id = %s"
        result = (option, text, id)
        self.cursor.execute(self.sql, result)
        self.conn.commit()
        self.cursor.close()

    def ListOptions(self):
        """
        get all options of database MySQL
        and show in list of options in web

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the options of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT id, opt, text FROM options"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()
        return self.result

    def GetOptions(self):
        """
        get all options of database MySQL for send to user
        in keyboard of Telegram Bot

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        result : list
            List with the options of database MySQL
        """
        self.cursor = self.conn.cursor()
        self.sql = "SELECT opt, text FROM options"
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()
        return self.result
