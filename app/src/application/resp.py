""" Module for manage the response of the bot to the user """

from application.users import User  # Import class User
from application.state_app import StateApp  # Import class StateApp
from application.api import Api  # Import class Api
from application.config_app import ConfigApp  # Import class configApp
from application.options import Options  # Import class Options


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
            result = self.config.TITULO_APP + \
                "Your response is "+text
            self.api.SendMessage(chatId, result)
            return self.api.SendKeyboard(chatId, self.options.GetOptions())
        elif text == 'ACTIVATE_SERVICE' or text == 'activate_service':
            if chatId == self.config.CHAT_ID_SOPORTE:
                self.state.ActivateState()
                result = self.config.TITULO_APP + \
                    "OK, SERVICE ACTIVATE"
                self.api.SendMessage(chatId, result)
        elif text == 'DEACTIVATE_SERVICE' or text == 'deactivate_service':
            if chatId == self.config.CHAT_ID_SOPORTE:
                self.state.DeactivateState()
                result = self.config.TITULO_APP + \
                    "OK, SERVICE DEACTIVATE"
                self.api.SendMessage(chatId, result)
        elif text == 'LIST_USERS':
            if chatId == self.config.CHAT_ID_SOPORTE:
                result = self.config.TITULO_APP + \
                    "LIST USERS: \n\n" \
                    + self.user.ListUsers()
                self.api.SendMessage(
                    self.config.CHAT_ID_SOPORTE, result)
        elif text == 'LIST_USERS_PENDING':
            if chatId == self.config.CHAT_ID_SOPORTE:
                result = self.config.TITULO_APP + \
                    "LIST USERS PENDING: \n\n" + \
                    self.user.ListUsersPending()
                self.api.SendMessage(
                    self.config.CHAT_ID_SOPORTE, result)
        elif text == 'LIST_USERS_AUTHORIZED':
            if chatId == self.config.CHAT_ID_SOPORTE:
                result = self.config.TITULO_APP + \
                    "LIST USERS AUTHORIZED: \n\n" + \
                    self.user.ListAuthorizedUsers()
                self.api.SendMessage(
                    self.config.CHAT_ID_SOPORTE, result)
        elif text == options[0][0]:
            result = self.config.TITULO_APP + options[0][1] + "\n"
            self.api.SendMessage(
                chatId, result)
        elif text == options[1][0]:
            result = self.config.TITULO_APP + options[1][1] + "\n"
            self.api.SendMessage(
                chatId, result)
        elif text == options[2][0]:
            result = self.config.TITULO_APP + options[2][1] + "\n"
            self.api.SendMessage(
                chatId, result)
        elif text == options[3][0]:
            result = self.config.TITULO_APP + options[3][1] + "\n"
            self.api.SendMessage(
                chatId, result)
        else:
            result = self.config.TITULO_APP + \
                "Sorry "+first_name + \
                ", I don't understand your message: ("+text+") \
                \n\nTry with /OPTIONS"
            self.api.SendMessage(chatId, result)
            keyboard = self.options.SendOptions()
            return self.api.SendKeyboard(chatId, keyboard)
