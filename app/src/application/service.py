""" Module for manage the service of the bot """

# Imports class necessary for the module
from application.resp import RespText
from application.api import Api
from application.config_app import ConfigApp
import json  # Import json for use json format
from application.users import User
from application.state_app import StateApp
from application.options import Options
from application.mongodb import MongoDB
from application.context import Context


class Service():
    """
    Class for manage the service of the bot

    Accept requests from Bot Telegram, save the data in a json file,
    read the data from the json file and process it,
    send the response to the user.

    """

    def __init__(self, data):
        """
        constructor for class

        args:
        ----------
        self : object
            Object of class
        data : dict
            Dictionary with the data of the message of the user
        """
        self.config = ConfigApp()
        self.token = self.config.TOKEN
        self.chat_id_support = self.config.CHAT_ID_SOPORTE
        self.email_support = self.config.EMAIL_SOPORTE
        self.meth = Api()
        self.user = User()
        self.state = StateApp()
        self.resp = RespText()
        self.options = Options()
        self.mongodb = MongoDB()
        self.context = Context()
        self.api = Api()

        json_file = 'data.json'  # File json for save data of message
        self.data = data

        # create file empty json if not exist
        with open(json_file, 'w') as file:
            file.write('')
        # add [] in file json
        with open(json_file, 'a') as file:
            file.write('[')
        # add data in file json
        with open(json_file, 'a') as file:
            json.dump(self.data, file)
        # close file with []
        with open(json_file, 'a') as file:
            file.write(']')
        # open file json and save in variable data
        with open(json_file) as file:
            self.data = json.load(file)
        # insert data in database MongoDB
        self.mongodb.InsertMessage(data)
        # if data is not empty
        if self.data != []:
            # for each data in file json
            for fact in self.data:
                try:
                    # Obtengo los parametros del mensaje
                    chatId = str(fact['message']['chat']['id'])
                    first_name = str(fact['message']['chat']['first_name'])
                    username = str(fact['message']['chat']['username'])
                    # date = fact['message']['date']
                    text = str(fact['message']['text'])
                    # save message in database MySQL
                    # self.user.SavedMessageUser(
                    #     chatId, first_name, text, username)
                except Exception:
                    print("Error: "+Exception)
                # send response to user
                # first check the state of the application
                actual_state = self.state.CheckState()
                actual_user = self.user.CheckUser(chatId)
                # if the user is not in the database, save it
                # and give him a welcome to the system as a new user
                # and send a message to admin to inform new user
                # if the user is in the database, check the service
                if actual_user == 0:
                    # saved the user in bd
                    self.user.SavedUser(chatId, first_name, username)
                    # send welcome message to user
                    self.resp.SendResponse(
                        chatId, "hola", first_name)
                    # send message to admin to inform new user
                    text = self.config.TITULO_APP +\
                        "New user in Bot: \n\n" + \
                        first_name + " - " + username + " ("+chatId+")"
                    self.meth.SendMessage(self.chat_id_support, text)
                else:
                    # if the service is out of service and
                    # the user is not admin
                    # we send a message to the user informing him that
                    # the service is out of service
                    if (actual_state == 0 and chatId != self.chat_id_support):
                        note = self.state.GetNoteState()
                        text = self.config.TITULO_APP+"Service out of service: \n\n" + \
                            note + "\n\nSorry for the inconvenience"
                        self.meth.SendMessage(chatId, text)
                    else:
                        # check if the user is authorized or is admin
                        # if it is authorized or admin, we send the resp
                        if self.user.ChekAuthorizedUser(chatId) == 1 or \
                                chatId == self.chat_id_support:
                            self.resp.SendResponse(
                                chatId, text, first_name)
                        # if the user is not authorized and is not admin
                        else:
                            # if the message is /SOLICITAR_ACCESO
                            # send a message to the admin
                            if text == '/REQUEST_ACCESS' \
                                    and chatId != self.chat_id_support:
                                if self.user.CheckRequestUser(chatId) == 0:
                                    text = self.config.TITULO_APP +\
                                        "Request access from user: \n\n" + \
                                        first_name + " - " + username +\
                                        " - ("+chatId+")"
                                    # update user's status to pending
                                    self.user.RequestUser(chatId)
                                    self.meth.SendMessage(
                                        self.chat_id_support, text)
                                    text = self.config.TITULO_APP + \
                                        "Your request has been sent to support, wait for a response.\n\n"
                                    self.meth.SendMessage(chatId, text)
                                else:
                                    text = self.config.TITULO_APP + \
                                        "Your request is pending, wait for a response.\n\n"
                                    self.meth.SendMessage(chatId, text)
                                    text = self.config.TITULO_APP\
                                        + "Remember that you have pending request.\n\n" +\
                                        first_name+" - " + username + \
                                        " - ("+chatId+")"
                                    self.meth.SendMessage(
                                        self.chat_id_support, text)
                            else:
                                text = self.config.TITULO_APP +\
                                    "Sorry user "+first_name + \
                                    ", but you are not user authorized.\nRequest your access if you think it is necessary\n\n/REQUEST_ACCESS"
                                self.meth.SendMessage(chatId, text)
                # empty file json for accept new data
                with open(json_file, 'w') as file:
                    file.write('')
