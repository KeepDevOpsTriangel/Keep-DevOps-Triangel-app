# src/tests/test_app.py

from unittest.mock import MagicMock, patch
from application.users import User
from application.config_app import ConfigApp

def test_list_users_web():
    # Configurar el mock de la conexión a la base de datos
    mock_conn = MagicMock()

    # Configurar el mock del resultado de la consulta a la base de datos
    mock_result = [(1, 'kc', 'triangle', 'kc.triangle@example.com')]
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = mock_result

    # Crear una instancia de User con el mock de la conexión
    user = User(conn=mock_conn)

    # Llamar a la función que deseamos probar
    result = user.ListUsersWeb()

    # Verificar que la función devuelve el resultado esperado
    assert result == mock_result

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

def test_default_apiurl_app():
    config = ConfigApp()
    assert config.APIURL == 'https://api.telegram.org/bot'

##################################################################################