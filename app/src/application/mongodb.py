""" Module for config app Telegram database MongoDB """

import pymongo  # Import pymongo for use MongoDB
from application.config_app import ConfigApp  # Import class ConfigApp


class MongoDB():
    """ Class for config app Telegram database MongoDB """

    def __init__(self):
        """ Constructor for class Mongo """
        self.config = ConfigApp()
        self.host = self.config.MONGO_HOST
        self.port = self.config.MONGO_PORT
        self.database = self.config.MONGO_DATABASE
        self.collection = self.config.MONGO_COLLECTION
        self.client = pymongo.MongoClient(f'mongodb://{self.host}:{self.port}')
        self.database = self.client[self.database]
        self.collection = self.database[self.collection]

    def InsertMessage(self, message):
        """ 
        Insert message in MongoDB

        args:

        message : dict
            Dictionary with the data of the message of the user
        """
        self.collection.insert_one(message)
