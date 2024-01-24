# docs_config.py

# Añade el directorio raíz de tu aplicación al PYTHONPATH
import sys
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(current_dir, 'app')
sys.path.insert(0, app_dir)

# Importa el módulo principal de tu aplicación
from app.src.app import app

# También puedes intentar importar el módulo application directamente si es un paquete
# from app import application  # Asegúrate de reemplazar "application" con el nombre correcto

# Indica a pdoc los módulos que debe documentar
modules = [app]
