from .settings import *
import os

# Production settings
DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "https://portfolio-ma77.onrender.com", # <--- ADD THIS LINE, replace with your actual Render URL
]

# Security
SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-r*vbx$28&d%g#*#t($%yc!4h)om=lx#q9e_z!tqgcayq3hzo+l"
)

# Static files configuration for production
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise configuration for serving static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Add WhiteNoise to middleware (insert after SecurityMiddleware)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Database (keeping SQLite for simplicity)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
