import redis

from application.config_app import ConfigApp


class Authenticator():

    def __init__(self, default_username, default_password):

        self.config = ConfigApp()
        self.redis_host = self.config.REDIS_HOST
        self.redis_client = redis.StrictRedis(
            host=self.redis_host, port=6379)
        self.redis_client.hset('users', default_username, default_password)

    def Login(self, username, password):
        stored_password = self.redis_client.hget('users', username)
        if stored_password and stored_password.decode('utf-8') == password:
            return True
        return False
