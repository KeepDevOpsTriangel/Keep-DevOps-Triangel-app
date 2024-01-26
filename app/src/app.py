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

load_dotenv()  # Load variables of .env


class MyApp():
    def __init__(self):
        self.app = Flask(__name__, template_folder='application/templates',
                         static_folder='application/static')
        self.config = ConfigApp()
        self.user = User()
        self.options = Options()
        self.state = StateApp()
        self.api = Api()
        self.title_web = self.config.TITULO_APP
        self.routes()

    def routes(self):
        @self.app.route('/', methods=['GET'])
        def Index_():
            """
            Method for render template page home.html

            return:
            ----------
            render_template : object
                Object of class render_template
                render template home.html
            """
            return render_template('home.html', title=self.title_web)

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

        @self.app.route('/webhook', methods=['GET', 'POST'])
        def WebHook_():
            """
            Method for manage the webhook of Telegram Bot

            return:
            ----------
            AppWeb.WebHook : object
                Object of class AppWeb
                manage the webhook of Telegram Bot
            """
            return AppWeb.WebHook(self)

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

    def RunApp(self):
        """
        Method for run the app
        """
        self.app.run(debug=True)


WebApp = MyApp()
app = WebApp.app
if __name__ == "__main__":
    WebApp.RunApp()  # Run the app