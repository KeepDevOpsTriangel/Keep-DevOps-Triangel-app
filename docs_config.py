# docs_config.py

# Configuración para pdoc
# Aquí debes incluir todas las configuraciones necesarias para que pdoc pueda importar y documentar tu código.

# Añade el directorio raíz de tu aplicación al PYTHONPATH
import sys
sys.path.insert(0, './app')

# Importa el módulo principal de tu aplicación
from app.src.app import app  # Asegúrate de reemplazar "YourMainModule" con el nombre correcto

# Indica a pdoc los módulos que debe documentar
modules = [app]  # Asegúrate de reemplazar "YourMainModule" con el nombre correcto
