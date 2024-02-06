""" Module for web app. """

import requests
from flask import render_template, request, session
from application.users import User
from application.config_app import ConfigApp
from application.state_app import StateApp
from application.options import Options
from application.api import Api
from application.service import Service
from application.auth import Authenticator
from application.mongodb import MongoDB
from application.context import Context


class AppWeb():
    """
    class for web app
    """

    def __init__(self):
        """
        Constructor for class
        """
        self.api = Api()
        self.config = ConfigApp()
        self.options = Options()
        self.state = StateApp()
        self.user = User()
        self.authenticator = Authenticator()
        self.title_web = self.config.TITULO_APP  # Define title of web app
        self.mongodb = MongoDB()
        self.context = Context()

    def Index(self):
        """
        webhook for Bot Telegram where
        receive the messages of the users
        and are processed by the Bot Telegram API

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template home.html
        """
        if request.method == 'POST':
            Service(request.json)
            return render_template('home.html')
        if request.method == 'GET':
            if 'username' in session:
                return render_template('home.html', title=self.title_web,
                                       myuser=session['username'])
            else:
                return render_template('login.html', title=self.title_web)

    def GetWebHookInfo(self):
        """
        get webhook info of Bot Telegram API

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template get_webhook.html
        """
        if 'username' in session:
            api_url = self.config.APIURL+self.config.TOKEN+"/getWebhookInfo"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                return render_template('get_webhook.html', data=data,
                                       title=self.title_web,
                                       myuser=session['username'])
            else:
                return render_template('get_webhook.html', error=response)
        else:
            return render_template('login.html', title=self.title_web)

    def DeleteWebHook(self):
        """
        delete webhook of Bot Telegram API

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template home.html
        """
        if 'username' in session:
            api_url = self.config.APIURL+self.config.TOKEN+"/deleteWebhook"
            response = requests.get(api_url)
            if response.status_code == 200:
                resp = response.json()
                return render_template('home.html', resp=resp,
                                       title=self.title_web,
                                       myuser=session['username'])
            else:
                return render_template('get_webhook.html', error=response)
        else:
            return render_template('login.html', title=self.title_web)

    def SetWebHook(self):
        """
        set webhook of Bot Telegram API

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template home.html
        """
        if 'username' in session:
            api_url = self.config.APIURL+self.config.TOKEN + \
                "/setWebhook?url="+self.config.URL_WEBHOOK
            response = requests.post(api_url)
            if response.status_code == 200:
                resp = response.json()
                return render_template('home.html',
                                       resp=resp, title=self.title_web,
                                       myuser=session['username'])
            else:
                return render_template('get_webhook.html',
                                       error=response)
        else:
            return render_template('login.html', title=self.title_web)

    def ListUsersWebApp(self):
        """
        list users of database MySQL in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template users.html
        """
        if 'username' in session:
            users = self.user.ListUsersWeb()
            return render_template('users.html',
                                   users=users, title=self.title_web,
                                   myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)

    def ListOptionsWebApp(self):
        """
        list options of database MySQL in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template options.html
        """
        if 'username' in session:
            options = self.options.ListOptions()
            return render_template('options.html',
                                   options=options, title=self.title_web,
                                   myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)

    def EditOptionsWebApp(self, id):
        """
        edit option of database MySQL in web app

        args:
        ----------
        self : object
            Object of class
        id : int
            Id of option

        return:
        ----------
        render_template : object
            Object of class render_template
            render template options.html
        """
        if 'username' in session:
            if request.method == 'POST':
                id = request.form['id']
                option = request.form['option']
                text = request.form['text']
                self.options.EditOptions(id, option, text)
                options = self.options.ListOptions()
                message = option+" edited correctly."
                return render_template('options.html', options=options,
                                       message=message, title=self.title_web,
                                       myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)

    def ActivateDeactivateUserWebApp(self, id, first_name, chatId, state):
        """
        method for activate or deactivate user in web app

        if state is 1, deactivate user in database MySQL
        and send message to user in Telegram Bot.
        if state is 0, activate user in database MySQL
        and send message to user in Telegram Bot.

        args:
        ----------
        self : object
            Object of class
        id : int
            Id of user
        first_name : str
            First name of user
        chatId : str
            Id of chat user
        state : int
            State of user

        return:
        ----------
        render_template : object
            Object of class render_template
            render template users.html
        """
        if 'username' in session:
            if request.method == 'POST':
                id = request.form['id']
                first_name = request.form['first_name']
                chatId = request.form['chatId']
                state = request.form['state']
                if (state == "1"):
                    self.user.DeactivateUserWeb(id)
                    message = "User " + first_name + \
                        " deactivated correctly and informed by Telegram."
                    self.api.SendMessage(
                        chatId, "Hello "+first_name+", your user has been deactivated.\nYou can't use the Bot.")
                else:
                    self.user.ActivateUserWeb(id)
                    message = "User " + first_name + \
                        " activated correctly and informed by Telegram."
                    self.api.SendMessage(
                        chatId, "Hello "+first_name+", your user has been activated.\nYou can use the Bot.")
                users = self.user.ListUsersWeb()
                return render_template('users.html', users=users,
                                       message=message, title=self.title_web,
                                       myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)

    def ServiceStateWebApp(self):
        """
        get service state of web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template service.html
        """
        if 'username' in session:
            if request.method == 'GET':
                note = self.state.GetNoteState()
                result = self.state.CheckStateWeb()
                return render_template('service.html',
                                       result=result, note=note,
                                       title=self.title_web,
                                       myuser=session['username'])
            if request.method == 'POST':
                result = self.state.CheckStateWeb()
                if result == 0:
                    self.state.ActivateState()
                    result = self.state.CheckStateWeb()
                    for row in self.user.ChatIdUsers():
                        chatId = row[0]
                        self.api.SendMessage(
                            chatId, "The service has been activated. \n\nYou can use the Bot.")
                    return render_template('service.html', result=result)
                else:
                    new_note = request.form['note']
                    self.state.UpdateNoteState(new_note)
                    note = self.state.GetNoteState()
                    self.state.DeactivateState()
                    result = self.state.CheckStateWeb()
                    for row in self.user.ChatIdUsers():
                        chatId = row[0]
                        self.api.SendMessage(
                            chatId, "Service temporarily unavailable: \n\n" + note +
                                    "\n\nSorry for the inconvenience.")
                    return render_template('service.html',
                                           result=result, note=note)
        else:
            return render_template('login.html', title=self.title_web)

    def SendMessagesWebApp(self):
        """
        send messages to users to Bot Telegram
        from web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template send_messages.html
        """
        if 'username' in session:
            if request.method == 'GET':
                users = self.user.ListUsersWeb()
                return render_template('send_messages.html',
                                       users=users, title=self.title_web,
                                       myuser=session['username'])
            if request.method == 'POST':
                chatId = request.form['chatId']
                message = self.title_web + request.form['message']
                self.api.SendMessage(chatId, message)
                users = self.user.ListUsersWeb()
                return render_template('send_messages.html',
                                       message="Message sent correctly.",
                                       users=users, title=self.title_web)
        else:
            return render_template('login.html', title=self.title_web)

    def GetMessagesWebApp(self):
        """
        get messages of users from Bot Telegram
        saved in database MySQL
        and show in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template messages.html
        """
        if 'username' in session:
            # messages = self.user.ListMessagesWeb()
            messages = self.mongodb.GetMessages()
            return render_template('messages.html',
                                   messages=messages, title=self.title_web,
                                   myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)

    def Login(self):
        """
        login in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template login.html
        """
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if self.authenticator.Login(username, password):
                session['username'] = username
                return render_template('home.html', title=self.title_web,
                                       myuser=session['username'])
            else:
                return render_template('login.html', title=self.title_web,
                                       resp="Login failed.")
        else:
            return render_template('home.html', title=self.title_web)

    def LogOut(self):
        """
        logout in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template login.html
        """
        session.pop('username', None)
        return render_template('login.html', title=self.title_web)

    def ChatBot(self):
        """
        config chatbot in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template context.html
        """
        if 'username' in session:
            if request.method == 'GET':
                mycontext = self.context.GetContext()
                return render_template('context.html', mycontext=mycontext,
                                       title=self.title_web,
                                       myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)

    def SetChatBot(self):
        """
        set context of chatbot in web app

        args:
        ----------
        self : object
            Object of class

        return:
        ----------
        render_template : object
            Object of class render_template
            render template context.html
        """
        if 'username' in session:
            if request.method == 'POST':
                context = request.form['context']
                self.context.SetContext(context)
                mycontext = self.context.GetContext()
                return render_template('context.html', mycontext=mycontext,
                                       message="Context set correctly.",
                                       title=self.title_web,
                                       myuser=session['username'])
        else:
            return render_template('login.html', title=self.title_web)
