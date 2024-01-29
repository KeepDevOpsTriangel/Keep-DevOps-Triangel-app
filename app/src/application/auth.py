""" This module is responsible for authenticating users using redis. """
import redis

from application.config_app import ConfigApp


class Authenticator():
    """
    Class for methods of authentication
    """

    def __init__(self, default_username, default_password):
        """
        Constructor for Authenticator class
        """
        self.config = ConfigApp()
        self.redis_host = self.config.REDIS_HOST
        self.redis_client = redis.StrictRedis(
            host=self.redis_host, port=6379)
        self.redis_client.hset('users', default_username, default_password)

    def Login(self, username, password):
        """
        Method for authentication user.
        Check if the username and password are correct.
        Return True if authentication is successful, False otherwise.

        Args:
            username (str): username of user
            password (str): password of user

        Returns:
            bool: True if authentication is successful, False otherwise   
        """
        stored_password = self.redis_client.hget('users', username)
        if stored_password and stored_password.decode('utf-8') == password:
            return True
        return False
