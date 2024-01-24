# Añade el directorio raíz de tu aplicación al PYTHONPATH
import sys
sys.path.insert(0, './app')

# Importa el módulo principal de tu aplicación
from app.src.app import app

# Indica a pdoc los módulos que debe documentar
modules = [app]