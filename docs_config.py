# docs_config.py

# Añade el directorio raíz de tu aplicación al PYTHONPATH
import sys
sys.path.insert(0, './app')

# Importa el módulo principal de tu aplicación
from app.src.app import app  # Asegúrate de reemplazar "YourMainModule" con el nombre correcto

# Importa el módulo application
import application  # Asegúrate de reemplazar con el nombre correcto

# Indica a pdoc los módulos que debe documentar
modules = [app, application]  # Asegúrate de reemplazar "YourMainModule" con el nombre correcto
