""" File main for run the app Python Flask """

from dotenv import load_dotenv  # Import load_dotenv for load variables of .env
# Import Flask for create web app
from flask import Flask, request, render_template
# Import functions of modules of app
from application.web import AppWeb
from application.config_app import ConfigApp
from application.users import User
from application.options import Options
from application.state_app import StateApp
from application.api import Api
from application.auth import Authenticator
from application.mongodb import MongoDB
from application.context import Context
import os

load_dotenv()  # Load variables of .env


class MyApp():
    def __init__(self):
        self.app = Flask(__name__, template_folder='application/templates')
        self.config = ConfigApp()
        self.user = User()
        self.options = Options()
        self.state = StateApp()
        self.api = Api()
        self.authenticator = Authenticator(
            self.config.WEB_USERNAME, self.config.WEB_PASSWORD)
        self.title_web = self.config.TITULO_APP
        self.mongodb = MongoDB()
        self.context = Context()
        self.routes()

    def routes(self):
        @self.app.route('/', methods=['GET', 'POST'])
        def Index_():
            """
            Method for render template page home.html

            return:
            ----------
            render_template : object
                Object of class render_template
                render template home.html
            """
            return AppWeb.Index(self)

        @self.app.errorhandler(404)
        def GetError404_(error):
            """
            Method for render template page 404.html

            return:
            ----------
            render_template : object
                Object of class render_template
                render template 404.html
            """
            return render_template('404.html', title=self.title_web)

        @self.app.route('/get_webhook', methods=['GET'])
        def GetWebHookInfo_():
            """
            Method for get the webhook info of Telegram Bot

            return:
            ----------
            AppWeb.GetWebHookInfo : object
                Object of class AppWeb
                get the webhook info of Telegram Bot
            """
            return AppWeb.GetWebHookInfo(self)

        @self.app.route('/set_webhook', methods=['POST'])
        def SetWebHook_():
            """
            Method for set the webhook of Telegram Bot

            return:
            ----------
            AppWeb.SetWebHook : object
                Object of class AppWeb
                set the webhook of Telegram Bot
            """
            return AppWeb.SetWebHook(self)

        @self.app.route('/delete_webhook', methods=['GET'])
        def DeleteWebHook_():
            """
            Method for delete the webhook of Telegram Bot

            return:
            ----------
            AppWeb.DeleteWebHook : object
                Object of class AppWeb
                delete the webhook of Telegram Bot
            """
            return AppWeb.DeleteWebHook(self)

        @self.app.route('/users', methods=['GET'])
        def ListUsersWebApp_():
            """
            Method for list the users of Telegram Bot

            return:
            ----------
            AppWeb.ListUsersWebApp : object
                Object of class AppWeb
                list the users of Telegram Bot
            """
            return AppWeb.ListUsersWebApp(self)

        @self.app.route('/options', methods=['GET'])
        def ListOptionsWebApp_():
            """
            Method for list the options of Telegram Bot

            return:
            ----------
            AppWeb.ListOptionsWebApp : object
                Object of class AppWeb
                list the options of Telegram Bot
            """
            return AppWeb.ListOptionsWebApp(self)

        @self.app.route('/edit_option', methods=['POST'])
        def EditOptionsWebApp_():
            """
            Method for edit the options of Telegram Bot

            return:
            ----------
            AppWeb.EditOptionsWebApp : object
                Object of class AppWeb
                edit the options of Telegram Bot
            """
            return AppWeb.EditOptionsWebApp(self, id)

        @self.app.route('/act_deact_user', methods=['POST'])
        def ActivateDeactivateUserWebApp_():
            """
            Method for activate or deactivate the users of Telegram Bot

            args:
            ----------
            self : object
                Object of class
            first_name : str
                First name of user
            id : str
                Id of user
            state : str
                State of user
            chatId : str
                Id of chat user

            return:
            ----------
            AppWeb.ActivateDeactivateUserWebApp : object
                Object of class AppWeb
                activate or deactivate the users of Telegram Bot
            """
            first_name = request.form['first_name']
            id = request.form['id']
            state = request.form['state']
            chatId = request.form['chatId']
            return AppWeb.ActivateDeactivateUserWebApp(self, first_name,
                                                       id, state, chatId)

        @self.app.route('/service', methods=['POST', 'GET'])
        def ServiceStateWebApp_():
            """
            Method for manage the service state of Telegram Bot

            return:
            ----------
            AppWeb.ServiceStateWebApp : object
                Object of class AppWeb
                manage the service state of Telegram Bot
            """
            return AppWeb.ServiceStateWebApp(self)

        @self.app.route('/send_messages', methods=['POST', 'GET'])
        def SendMessagesWebApp_():
            """
            Method for send messages to users of Telegram Bot

            return:
            ----------
            AppWeb.SendMessagesWebApp : object
                Object of class AppWeb
                send messages to users of Telegram Bot  
            """
            return AppWeb.SendMessagesWebApp(self)

        @self.app.route('/messages', methods=['GET'])
        def GetMessagesWebApp_():
            """
            Method for list the messages of Telegram Bot

            return:
            ----------
            AppWeb.GetMessagesWebApp : object
                Object of class AppWeb
                list the messages of Telegram Bot
            """
            return AppWeb.GetMessagesWebApp(self)

        @self.app.route('/login', methods=['GET', 'POST'])
        def Login_():
            """
            Method for login of the app

            return:
            ----------
            AppWeb.Login : object
                Object of class AppWeb
                login of the app
            """
            return AppWeb.Login(self)

        @self.app.route('/logout', methods=['GET'])
        def LogOut_():
            """
            Method for logout of the app

            return:
            ----------
            AppWeb.Logout : object
                Object of class AppWeb
                logout of the app
            """
            return AppWeb.LogOut(self)

        @self.app.route('/chatbot', methods=['GET'])
        def ChatBot_():
            """
            Method for render template page chatbot.html

            return:
            ----------
            render_template : object
                Object of class render_template
                render template chatbot.html
            """
            return AppWeb.ChatBot(self)

        @self.app.route('/setchatbot', methods=['POST'])
        def SetChatBot_():
            """
            Method for set the context of the chatbot

            return:
            ----------
            AppWeb.SetChatBot : object
                Object of class AppWeb
                set the context of the chatbot
            """
            return AppWeb.SetChatBot(self)

    def RunApp(self):
        """
        Method for run the app
        """
        self.app.run(debug=True)


WebApp = MyApp()
app = WebApp.app
app.secret_key = os.urandom(24)
if __name__ == "__main__":
    WebApp.RunApp()  # Run the app
