# docs_config.py

import sys
import os

# Añade el directorio raíz de tu aplicación al PYTHONPATH
current_dir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(current_dir, 'app')
sys.path.insert(0, app_dir)

# Importa el módulo principal de tu aplicación
from app.src.app import app  # Modifica esta línea

# Indica a pdoc los módulos que debe documentar
modules = [app]