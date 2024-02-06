""" Module for manage the response of the bot to the user """

from openai import OpenAI  # Import OpenAI for use the API
from application.users import User  # Import class User
from application.state_app import StateApp  # Import class StateApp
from application.api import Api  # Import class Api
from application.config_app import ConfigApp  # Import class configApp
from application.options import Options  # Import class Options
from application.context import Context  # Import class Context


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
        self.client = OpenAI(api_key=self.config.OPENAI_API_KEY)
        self.context = Context()
        self.model = "gpt-3.5-turbo-instruct"
        self.temperature = 0.5
        self.max_tokens = 150

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
            return self.api.SendKeyboard(chatId, self.options.GetOptions())
        elif text == 'hola':
            result = self.config.TITULO_APP + "Hola " + first_name + "\n"
            self.api.SendMessage(chatId, result)
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
            mycontext = self.context.GetContextContext()
            prompt = mycontext + "\n" + text
            prompt = f"{mycontext}\n{text}" if mycontext else prompt
            response = self.client.completions.create(
                model=self.model,
                prompt=prompt,
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            myanswer = response.choices[0].text.strip()
            mycontext = myanswer
            result = self.config.TITULO_APP + myanswer
            self.api.SendMessage(chatId, result)
            keyboard = self.options.SendOptions()
            return self.api.SendKeyboard(chatId, keyboard)
