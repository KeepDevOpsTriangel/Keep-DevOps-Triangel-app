""" Module for config chatbot with OpenAI """

from openai import OpenAI  # Import OpenAI for use the API
from application.config_app import ConfigApp  # Import class configApp
from application.context import Context  # Import class Context


class ChatBot():
    """ Class for config chatbot with OpenAI """

    def __init__(self):
        """
        Constructor for class

        Obtain the class Api, ConfigApp
        from the package application.
        """
        self.config = ConfigApp()
        self.client = OpenAI(api_key=self.config.OPENAI_API_KEY)
        self.context = Context()
        self.mycontext = self.context.GetContextContext()
        self.model = "gpt-3.5-turbo-instruct"
        self.temperature = 0.9
        self.max_tokens = 100

    def ChatBotResponse(self, text):
        """
        openai chatbot response to user
        
        args:
        ----------
        self : object
            Object of class
        text : str
            Text of message
        
        return:
        ----------
        result : str
            Text of message
        """
        prompt = self.mycontext
        prompt = f"{self.mycontext}\n{text}" if self.mycontext else prompt
        response = self.client.completions.create(
            model=self.model,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        myanswer = response.choices[0].text.strip() + "..."
        if response.choices[0].finish_reason == 'length':
            myanswer += "\n\n" + "Solicitáme más información..."
        self.mycontext = text + myanswer
        result = self.config.TITULO_APP + myanswer
        return result
