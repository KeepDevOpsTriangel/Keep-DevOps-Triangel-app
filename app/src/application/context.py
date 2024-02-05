""" Module for context of the application. """

import pymysql  # import pymysql to connect to the database MySQL Python
# Import class configApp
from application.config_app import ConfigApp


class Context():
    """
    Class for the context of the application.
    It contains the config chatbot with openai
    Control the context of the chatbot
    """

    def __init__(self):
        """
        Constructor of the class.
        It creates the connection to the database MySQL Python
        and config data.
        """
        self.config = ConfigApp()  # Create an object of the class ConfigApp
        self.db = pymysql.connect(host=self.config.MYSQL_HOST,
                                  user=self.config.MYSQL_USER,
                                  password=self.config.MYSQL_PASSWORD,
                                  database=self.config.MYSQL_DATABASE)

    def GetContext(self):
        """
        Method for get the context of the chatbot.

        Returns:
            str: context of the chatbot
        """
        self.cursor = self.db.cursor()
        self.sql = 'SELECT title_context, context FROM context where id = 1'
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()
        return self.result

    def SetContext(self, title_context, context):
        """
        Method for set the context of the chatbot.

        Args:
            title_context (str): title of the context
            context (str): context of the chatbot
        """
        self.cursor = self.db.cursor()
        self.sql = f'UPDATE context SET \
            title_context = "{title_context}",\
            context = "{context}" WHERE id = 1'
        self.cursor.execute(self.sql)
        self.db.commit()
