""" Module with Methods of Telegram API """

from application.config_app import ConfigApp  # Import class configApp
import requests  # Import requests for use methods of API
import json  # Import json for use json format


class Api():
    """
    Class for methods Telegram API

    Use methods of Telegram API for send messages and keyboard.
    """

    def __init__(self):
        """
        Constructor for class

        Parameters
        ----------
        self : object
            Object of class
        config : object
            Object of class configuration
        """

        self.config = ConfigApp()
        self.ApiUrl = self.config.APIURL
        self.token = self.config.TOKEN
        self.chatIdSoporte = self.config.CHAT_ID_SOPORTE
        self.emailSoporte = self.config.EMAIL_SOPORTE
        self.tituloApp = self.config.TITULO_APP

    def SendMessage(self, chatId, text):
        """
        send message to user

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user
        text : str
            Text of message

        return:
        ----------
        requests.post : object
            Object of class requests
            send message to user
        """
        return requests.post(self.ApiUrl+self.token +
                             '/sendMessage', data={'chat_id': chatId,
                                                   'text': text})

    def SendKeyboard(self, chatId, keyboard):
        """
        send keyboard to user

        args:
        ----------
        self : object
            Object of class
        chatId : str
            Id of chat user
        text : str
            Text of message
        keyboard : str
            Keyboard of message

        return:
        ----------
        requests.post : object
            Object of class requests
            send keyboard to user
        """
        return requests.post(self.ApiUrl+self.token+'/sendMessage',
                             data={'chat_id': chatId, 'text': '/OPCIONES',
                                   'reply_markup': json.dumps(keyboard)})
