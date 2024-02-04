""" This is a chatbot that uses the GPT-3 model to answer questions. """

from openai import OpenAI  # Import OpenAI for use the API
# Import ConfigApp for use the config file
from application.config_app import ConfigApp


class ChatAI():
    """
    Class to create a chatbot that uses the GPT-3 model to answer questions.
    """

    def __init__(self):
        """
        constructor for class

        Initialize the connection to the API OpenAI
        """
        self.config = ConfigApp()  # Create an instance of ConfigApp
        self.client = OpenAI(api_key=self.config.OPENAI_API_KEY)
        self.mycontext = None
        self.model = "gpt-3.5-turbo-instruct"
        self.temperature = 0.5
        self.max_tokens = 150

    def AnswerChatAI(self, prompt):
        """
        function to answer the question with the GPT-3 model

        Args:
            prompt (str): question to be answered

        Returns:
            str: answer to the question
        """
        prompt = f"{self.mycontext}\n{prompt}" if self.mycontext else prompt
        response = self.client.completions.create(
            model=self.model,
            prompt=prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        myanswer = response.choices[0].text.strip()
        self.mycontext = myanswer
        return myanswer
