import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv  # ✅ Įkeliame .env failą

# ✅ Bazinė projekto direktorija
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Įkeliame .env failo reikšmes
load_dotenv()

# ✅ Django slapta rakto reikšmė iš .env (NEPALIK KODO VIDUJE!)
SECRET_KEY = os.getenv("SECRET_KEY", "default_saugus_raktas")

# ✅ Debug režimas (iš .env, kad būtų galima lengvai keisti tarp True/False)
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ Leidžiami hostai (įskaitant Railway)
ALLOWED_HOSTS = ["127.0.0.1", os.getenv("RAILWAY_URL", "")]

CSRF_TRUSTED_ORIGINS = ["https://web-production-39021.up.railway.app"]

# ✅ Įdiegtos Django programos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paytono_failai',  # Tavo Django aplikacija
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ URL konfigūracija
ROOT_URLCONF = 'projekto_modulis.urls'

# ✅ Django šablonai
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ✅ WSGI
WSGI_APPLICATION = 'projekto_modulis.wsgi.application'

# ✅ Duomenų bazės nustatymai (Railway suteikia `DATABASE_URL`)
DATABASES = {
    'default': dj_database_url.config(default=os.getenv("DATABASE_URL"))
}

# ✅ Slaptažodžių validacija
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Laiko zona ir kalba
LANGUAGE_CODE = 'lt'
TIME_ZONE = 'Europe/Vilnius'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ STATIC failai (teisingi nustatymai „Railway“)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ MEDIA failai (nuotraukoms ir kt.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Numatytoji pirminė raktų sistema
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ El. pašto nustatymai (Railway `.env` naudojimas)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = os.getenv("EMAIL_PORT", 587)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# ✅ Iš kur siųsti el. laiškus
DEFAULT_FROM_EMAIL = f"Paslaugų puslapis <{EMAIL_HOST_USER}>"