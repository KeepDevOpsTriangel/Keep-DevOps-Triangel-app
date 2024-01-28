# app/tests/test_app.py

from app.src.app import MyApp

def test_create_app():
    app = MyApp()
    assert app is not None
    # Agrega más aserciones según sea necesario

# Puedes agregar más tests para otras funciones en tu aplicación

# app/tests/test_users.py

from app.src.application.users import User

def test_create_user():
    user = User()
    assert user is not None
    # Agrega más aserciones según sea necesario

# Puedes agregar más tests para otras funciones relacionadas con usuarios
