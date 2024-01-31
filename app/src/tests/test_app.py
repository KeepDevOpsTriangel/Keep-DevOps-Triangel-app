from application.config_app import ConfigApp

##################################################################################

def test_default_titulo_app():
    config = ConfigApp()
    assert config.TITULO_APP == 'TRIANGLE-App' + '\n\n'

##################################################################################

def test_default_telf_app():
    config = ConfigApp()
    assert config.TELEFONO_SOPORTE == '900000000' + '\n\n'

##################################################################################
    
def test_default_chat_id_app():
    config = ConfigApp()
    assert config.CHAT_ID_SOPORTE == '000000' + '\n\n'

##################################################################################
    
def test_default_email_app():
    config = ConfigApp()
    assert config.EMAIL_SOPORTE == 'MyEMAIL' + '\n\n'

##################################################################################

def test_default_sql_host():
    config = ConfigApp()
    assert config.MYSQL_HOST == 'localhost'
    
##################################################################################
    
def test_default_sql_db():
    config = ConfigApp()
    assert config.MYSQL_DATABASE == 'databasemysql'

##################################################################################

def test_default_web_username():
    config = ConfigApp()
    assert config.WEB_USERNAME == 'userweb'

##################################################################################
