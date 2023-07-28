import os
from pathlib import Path
from typing import Dict

import dotenv

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {}

if (
    os.getenv("DB_NAME", None)
    and os.getenv("DB_USERNAME", None)
    and os.getenv("DB_PASSWORD", None)
    and os.getenv("DB_ENGINE", "").lower() == "mysql"
):
    DB_DEFAULT: Dict = {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", None),
        "USER": os.getenv("DB_USERNAME", None),
        "PASSWORD": os.getenv("DB_PASSWORD", None),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", ""),
        "OPTIONS": {
            "charset": "utf8mb4",
            # "ssl": {"ca": os.getenv("DB_SSL_CERT", None)},
        },
    }
else:
    DB_DEFAULT: Dict = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "dragon.sqlite3"),
    }

# Athena
if (
    os.getenv("ATHENA_USERNAME", None)
    and os.getenv("ATHENA_PASSWORD", None)
    and os.getenv("ATHENA_HOST", None)
):
    DB_ATHENA = {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "athena",
        "USER": os.getenv("ATHENA_USERNAME", None),
        "PASSWORD": os.getenv("ATHENA_PASSWORD", None),
        "HOST": os.getenv("ATHENA_HOST", None),
        "PORT": os.getenv("ATHENA_PORT", ""),
        "OPTIONS": {
            "charset": "utf8mb4",
            "ssl": {"ca": os.getenv("ATHENA_SSL_CERT", None)},
        },
    }
else:
    dbpath = os.path.join(BASE_DIR, "athena.sqlite3")
    DB_ATHENA = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.getenv("ATHENA_DB_PATH", dbpath),
    }

DATABASES = {
    "default": DB_DEFAULT,
    "athena": DB_ATHENA,
}
