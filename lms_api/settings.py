from pathlib import Path
import environ

# Initialize environment variables
env = environ.Env(DEBUG=(bool, False))

# Read the .env file
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# Load secret key from .env
SECRET_KEY = env("DJANGO_SECRET_KEY")

# Load debug mode from .env
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "corsheaders",
    "main",
    "rest_framework",
    "rest_framework.authtoken",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Must be before CommonMiddleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lms_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "lms_api.wsgi.application"

# Database configuration from .env
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# AWS S3 Configuration from .env
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    # Media file (image) management
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}

# Stripe keys from .env
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY")

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_URL = "http://localhost:3000"

CORS_ALLOW_ALL_ORIGINS = True  # Remove CORS_ALLOWED_ORIGINS to avoid conflicts

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
