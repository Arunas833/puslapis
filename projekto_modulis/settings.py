import os
from pathlib import Path
from dotenv import load_dotenv  # ✅ Įkeliame dotenv, kad galėtume naudoti .env failą

# Bazinė projekto direktorija
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Įkeliame .env failo reikšmes
load_dotenv()

# ✅ Slapta Django rakto reikšmė iš .env (NEPALIK kodo viduje!)
SECRET_KEY = os.getenv("SECRET_KEY", "pakeisk-į-saugią-reikšmę")

# ✅ Debug režimas (iš .env, kad būtų galima lengvai keisti tarp True/False)
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ Leidžiami hostai (iš .env, galima pridėti kelis)
ALLOWED_HOSTS = ["*"]

# Įdiegtos programos
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'paytono_failai',  # Mūsų sukurta aplikacija
]

# Vidurinė programinė įranga (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL konfigūracija
ROOT_URLCONF = 'projekto_modulis.urls'

# Šablonų nustatymai
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # ✅ Teisingas kelias į šablonus
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

# WSGI programa
WSGI_APPLICATION = 'projekto_modulis.wsgi.application'

# ✅ Duomenų bazės nustatymai (jei naudosime PostgreSQL ar kitą DB)
DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        'NAME': os.getenv("DATABASE_NAME", BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv("DATABASE_USER", ""),
        'PASSWORD': os.getenv("DATABASE_PASSWORD", ""),
        'HOST': os.getenv("DATABASE_HOST", ""),
        'PORT': os.getenv("DATABASE_PORT", ""),
    }
}

# Slaptažodžių validacija
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Tarptautizacija
LANGUAGE_CODE = 'lt'
TIME_ZONE = 'Europe/Vilnius'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ STATIC failai
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # ✅ Sutvarkytas kelias
STATIC_ROOT = BASE_DIR / "staticfiles"

# ✅ MEDIA failai (nuotraukoms ir kt.)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Numatytoji pirminė raktų sistema
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ El. pašto nustatymai (visi slapti duomenys perkelti į .env)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "tavopastas@gmail.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

DEFAULT_FROM_EMAIL = f"Paslaugų puslapis <{EMAIL_HOST_USER}>"

