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
        self.model = "gpt-3.5-turbo-instruct"
        self.temperature = 0.5
        self.max_tokens = 150

    def ChatBotResponse(self, text):
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
        return result
