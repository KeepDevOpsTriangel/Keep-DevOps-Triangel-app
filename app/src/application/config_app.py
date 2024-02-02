""" Module for config app Telegram and database MySQL and Redis """

import os  # Import os for use variables of environment
# Import load_dotenv for load variables of environment
from dotenv import load_dotenv

load_dotenv()  # Load variables of environment


class ConfigApp():
    """
    Config class for app Telegram and database MySQL and Redis.

    Parameters with os.getenv() are variables of environment
    in file .env in root of project.
    Save the variables for use in class and methods of app.

    args:
    ----------
    URL_WEBHOOK : str
        Url for webhook
    APIURL : str
        Url for API Telegram
    TOKEN : str
        Token of bot
    TITULO_APP : str
        Title of app
    TELEFONO_SOPORTE : str
        Phone of support
    CHAT_ID_SOPORTE : str
        Chat id of support
    EMAIL_SOPORTE : str
        Email of support
    WEB_USERNAME : str
        Username of web flask app
    WEB_PASSWORD : str
        Password of web flask app
    MYSQL_HOST : str
        Host of database
    MYSQL_USER : str
        User of database
    MYSQL_PASSWORD : str
        Password of database
    MYSQL_NAME : str
        Name of database
    MYSQL_PORT : str
        Port of database
    REDIS_HOST : str
        Host of Redis database
    """
    URL_WEBHOOK = os.getenv('URL_WEBHOOK')
    APIURL = os.getenv('API_TELEGRAM')
    TOKEN = os.getenv('TOKEN')
    TITULO_APP = os.getenv('TITULO_APP', 'TRIANGLE-App') + '\n\n'
    TELEFONO_SOPORTE = os.getenv(
        'TELEFONO_SOPORTE', '900000000') + '\n\n'
    CHAT_ID_SOPORTE = os.getenv(
        'CHAT_ID_SOPORTE', '000000') + '\n\n'
    EMAIL_SOPORTE = os.getenv('EMAIL_SOPORTE', 'MyEMAIL') + '\n\n'
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'usermysql')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'passwordmysql')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'databasemysql')
    MYSQL_PORT = os.getenv('MYSQL_PORT', 3306)
    WEB_USERNAME = os.getenv('WEB_USERNAME', 'userweb')
    WEB_PASSWORD = os.getenv('WEB_PASSWORD', 'passwordweb')
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
    MONGO_PORT = os.getenv('MONGO_PORT', 27017)
    MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'databasemongo')
    MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'collectionmongo')
