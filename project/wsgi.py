import os
import sys
from pathlib import Path

import dotenv
from django.core.wsgi import get_wsgi_application


def addpath(path):
    if path not in sys.path:
        sys.path.insert(0, path)


CURR_DIR = Path(__file__).resolve(strict=True).parent
dotenv.load_dotenv(Path(CURR_DIR, ".env"))

if hasattr(CURR_DIR, "startswith"):
    BASE_DIR = CURR_DIR.parent
else:
    BASE_DIR = str(CURR_DIR.parent)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

# Add the project to the PYTHONPATH
os.environ.setdefault("DJANGO_PYTHON_PATH", BASE_DIR)
addpath(BASE_DIR)

try:
    application = get_wsgi_application()
except Exception as e:
    application = None
    print("Could not load WSGI application")
    print(e)
