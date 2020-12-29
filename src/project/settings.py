import os
from pathlib import Path

import dj_database_url
from django.urls import reverse_lazy
from dynaconf import settings as dyn

_this_file = Path(__file__).resolve()

DIR_PROJECT = _this_file.parent.resolve()

DIR_SRC = DIR_PROJECT.parent.resolve()

DIR_REPO = DIR_SRC.parent.resolve()

SECRET_KEY = dyn.SECRET_KEY

DEBUG = dyn.MODE_DEBUG

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    dyn.HOST,
] + list(dyn.ALLOWED_HOSTS or [])


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # ----my app ------
    "application.landing.apps.LandingConfig",
    "application.hello.apps.HelloConfig",
    "application.blog.apps.BlogConfig",
    "application.onboarding.apps.OnboardingConfig",
    "social_django",
]

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

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [DIR_PROJECT / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",  # Добавил эту строку
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE_URL = os.getenv("DATABASE_URL", dyn.DATABASE_URL)

DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []

LOGIN_URL = reverse_lazy("onboarding:sign-in")
LOGIN_REDIRECT_URL = reverse_lazy("landing:index")

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = "/static/"
STATIC_URL = "/s/"

STATIC_ROOT = DIR_REPO / ".static"

STATICFILES_DIRS = [
    DIR_PROJECT / "static",
]

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
AUTHENTICATION_BACKENDS = (
    "social_core.backends.telegram.TelegramAuth",  # Telegram
    "social_core.backends.vk.VKOAuth2",  # бекенд авторизации через ВКонтакте
    "django.contrib.auth.backends.ModelBackend",  # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
)
SOCIAL_AUTH_VK_OAUTH2_KEY = (
    "96f829d796f829d796f829d763968d592f996f896f829d7c92c82dee2dc8b013ed5a4ce"
)
SOCIAL_AUTH_VK_OAUTH2_SECRET = "7jhanAMZtdaEZ3dAhx0z"

SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = "1459498315:AAFv5cBE1IwzDJZo9mzYsW5FoKP6wM1Opk4"
