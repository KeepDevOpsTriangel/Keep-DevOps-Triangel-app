# src/tests/test_app.py

from application.users import User
from application.config_app import ConfigApp

##################################################################################

def test_default_titulo_app():
    config = ConfigApp()
    assert config.TITULO_APP == 'Valor_Predeterminado\n\n'

##################################################################################

def test_default_telf_app():
    config = ConfigApp()
    assert config.TELEFONO_SOPORTE == 'Valor_Predeterminado\n\n'

##################################################################################
    
def test_default_chat_id_app():
    config = ConfigApp()
    assert config.CHAT_ID_SOPORTE == 'Valor_Predeterminado\n\n'

##################################################################################
    
def test_default_email_app():
    config = ConfigApp()
    assert config.EMAIL_SOPORTE == 'Valor_Predeterminado\n\n'

##################################################################################