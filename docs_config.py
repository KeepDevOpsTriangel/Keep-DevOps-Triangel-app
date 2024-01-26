import sys
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
app_dir = os.path.join(current_dir, 'app')
sys.path.insert(0, app_dir)

from app.src.app import app

modules = [app]
