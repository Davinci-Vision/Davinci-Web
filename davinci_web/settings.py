import os
import json
from django.utils.translation import ugettext_lazy as _
from collections import namedtuple

from davinci_web import secret

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "davinci.vision"
]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',
    'board',
    'core',
    'django_summernote',
    'storages',
    'rosetta'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'davinci_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'davinci_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': secret.DATABASE_ENGINE,
        'NAME': secret.DATABASE_NAME,
        'HOST': secret.DATABASE_HOST,
        'PORT': secret.DATABASE_PORT,
        'USER': secret.DATABASE_USER,
        'PASSWORD': secret.DATABASE_PASSWORD
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ko-KR'
TIME_ZONE = 'Asia/Seoul'

LANGUAGES = [  # Available languages
    ('ko', _("Korean")),
    ('en', _("English")),
    ('zh', _("Chinese")),
    ('ja', _("Japan")),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static/")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# DEBUG ENV
if not DEBUG:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
else:
    # PRODUCTION ENV
    AWS_REGION = secret.AWS_REGION
    AWS_STORAGE_BUCKET_NAME = secret.AWS_STORAGE_BUCKET_NAME
    AWS_S3_HOST = "s3.%s.amazonaws.com" % AWS_REGION
    AWS_ACCESS_KEY_ID = secret.AUTH_ACCESS["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = secret.AUTH_ACCESS["AWS_SECRET_ACCESS_KEY"]
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" %AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    AWS_CLOUDFRONT_DOMAIN = secret.AUTH_ACCESS["AWS_CLOUDFRONT_DOMAIN"]
    MEDIA_URL = secret.AUTH_ACCESS["MEDIA_URL"]
    DEFAULT_FILE_STORAGE = 'core.utils.MediaStorage'
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


SUMMERNOTE_CONFIG = {
        'lang': 'ko-KR',
        'width': '100%',
        'height': '700',
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'strikethrough']],
            ['fontname', ['fontname', 'fontsize', 'color', 'clear']],
            ['para', ['paragraph','height']],
            ['format', ['ul', 'hr', 'table']],
            ['insert', ['link', 'picture', 'video']],
            ['misc', ['codeview']],
        ],
        'attachment_filesize_limit': 20 * 1024 * 1024,
    }
