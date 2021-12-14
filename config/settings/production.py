import os

import django_heroku

from .base import *  # noqa
from .base import BASE_DIR, MIDDLEWARE

DEBUG = False

# ALLOWED_HOSTS must write seperated by coma in environment. For Example:
# ALLOWED_HOSTS=localhost,127.0.0.1,example.com
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOST").split(",")

STATIC_ROOT = BASE_DIR / "static"  # For django admin static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

django_heroku.settings(locals())
