# JWT Settings
from datetime import timedelta

from .env import env

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": env("SECRET_KEY"),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
