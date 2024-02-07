""" Module for manage the response of the bot to the user """

from application.users import User  # Import class User
from application.state_app import StateApp  # Import class StateApp
from application.api import Api  # Import class Api
from application.config_app import ConfigApp  # Import class configApp
from application.options import Options  # Import class Options
from application.context import Context  # Import class Context
from application.chatbot import ChatBot  # Import class ChatBot
from application.mongodb import MongoDB  # Import class MongoDB
import time  # Import time for use time
import datetime  # Import datetime for use datetime


class RespText():
    """ Class for manage the response of the bot to the user """

    def __init__(self):
        """
        Constructor for class

        Obtain the class Api, ConfigApp, Options, StateApp and user
        from the package application.
        """
        self.api = Api()
        self.config = ConfigApp()
        self.options = Options()
        self.state = StateApp()
        self.user = User()
        self.context = Context()
        self.chatbot = ChatBot()
        self.mongodb = MongoDB()

    def SaveMessage(self, text):
        """
        save message of chatbot in MongoDB

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user
        text : str
            Text of message
        """
        time_unix = int(time.time())
        time_text = datetime.datetime.fromtimestamp(time_unix)
        time_text = time_text.strftime('%d-%m-%Y %H:%M:%S')
        message = {
            "message": {
                "date": time_text,
                "text": text,
                "chat": {
                    "first_name": self.config.TITULO_APP,
                    "username": "ChatBot",
                }
            }
        }
        self.mongodb.InsertMessage(message)

    def SendResponse(self, chatId, text, first_name):
        """
        send response to user in Telegram Bot when user send a message to bot
        and manage the response of the bot to the user and send the options.
        The response of the bot to the user is according
        to the message sent by the user,
        depending on the message sent by the user,
        the bot will send a different response.

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user
        text : str
            Text of message
        first_name : str
            First name of user

        return:
        ----------
        requests.post : object
            Object of class requests
            send message to user
        """
        options = self.options.GetOptions()
        if text == '/OPTIONS' or text == '/options':
            result = self.config.TITULO_APP + first_name + \
                ", puedes seleccionar una de mis opciones\n"
            self.api.SendMessage(chatId, result)
            self.api.SendKeyboard(chatId, self.options.GetOptions())
        elif text == 'newuser':
            result = self.config.TITULO_APP + "Hola " + first_name + \
                ", Bienvenido al asistente virtual, ¿En qué puedo ayudarte? \n\nTambién puedes seleccionar una de mis opciones\n"
            self.api.SendMessage(chatId, result)
            self.api.SendMessage(chatId, '/OPTIONS')
            self.api.SendKeyboard(chatId, self.options.GetOptions())
        elif text == options[0][0]:
            result = self.config.TITULO_APP + options[0][1] + "\n"
            self.api.SendMessage(
                chatId, result)
            self.SaveMessage(result)
        elif text == options[1][0]:
            result = self.config.TITULO_APP + options[1][1] + "\n"
            self.api.SendMessage(
                chatId, result)
            self.SaveMessage(result)
        elif text == options[2][0]:
            result = self.config.TITULO_APP + options[2][1] + "\n"
            self.api.SendMessage(
                chatId, result)
            self.SaveMessage(result)
        elif text == options[3][0]:
            result = self.config.TITULO_APP + options[3][1] + "\n"
            self.api.SendMessage(
                chatId, result)
            self.SaveMessage(result)
        else:
            self.api.SendMessage(
                chatId, self.config.TITULO_APP +
                "Un momento, estoy pensando...")
            result = self.chatbot.ChatBotResponse(text)
            self.api.SendMessage(chatId, result)
