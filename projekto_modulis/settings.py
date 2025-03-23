import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Įkeliam .env failo reikšmes
load_dotenv()

# Bazinė projekto direktorija
BASE_DIR = Path(__file__).resolve().parent.parent

# Django slaptasis raktas
SECRET_KEY = os.getenv("SECRET_KEY", "default_slaptas_raktas")

# Debug režimas (produkcinėje aplinkoje reikia DEBUG=False)
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Leidžiami hostai (įtraukite Railway domeną)
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'web-production-39021.up.railway.app']

# CSRF apsauga
CSRF_TRUSTED_ORIGINS = ["https://web-production-39021.up.railway.app"]

# Django aplikacijos
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "paytono_failai",  # Jūsų aplikacija
]

# Middleware (pridedame WhiteNoise, kad aptarnautų statinius failus)
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

# URL konfigūracija
ROOT_URLCONF = "projekto_modulis.urls"

# Šablonai
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI aplikacija
WSGI_APPLICATION = "projekto_modulis.wsgi.application"

# Duomenų bazės nustatymai (Railway PostgreSQL)
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    raise ValueError("❌ DATABASE_URL nėra nustatytas! Patikrinkite .env failą.")

# Slaptažodžių validacija
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Kalbos ir laiko zonos nustatymai
LANGUAGE_CODE = "lt"
TIME_ZONE = "Europe/Vilnius"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC failai
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# MEDIA failai
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Numatytoji pirminė raktų sistema
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# El. pašto nustatymai
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Iš kur siųsti el. laiškus
DEFAULT_FROM_EMAIL = f"Paslaugų puslapis <{EMAIL_HOST_USER}>"
