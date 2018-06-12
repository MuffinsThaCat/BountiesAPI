"""
Django settings for helloworld project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('django_secret', 'secret')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('local', False) == 'true'
ENVIRONMENT = os.environ.get('environment', 'local')

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework_filters',
    'std_bounties',
    'analytics',
    'authentication',
    'notifications',
    'django_nose',
]

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-inclusive',
    '--cover-xml',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    'authentication.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'bounties.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['bounties/templates', 'notifications/templates'],
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

WSGI_APPLICATION = 'bounties.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bounties',
        'USER': os.environ.get('psql_user', 'postgres'),
        'PASSWORD': os.environ.get('psql_password'),
        'HOST': os.environ.get('psql_host', 'localhost'),
        'PORT': os.environ.get('psql_port', 5432),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


CACHE_MIDDLEWARE_SECONDS = 10000

rollbar_token = os.environ.get('rollbar_token', None)

ROLLBAR = {
    'access_token': rollbar_token,
    'environment': ENVIRONMENT,
    'root': os.getcwd(),
    'enabled': True if rollbar_token else False,
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'rollbar': {
            'access_token': rollbar_token,
            'class': 'rollbar.logger.RollbarHandler',
            'level': 'WARNING',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'level': 'INFO',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['rollbar', 'console'],
            'propagate': True,
        },
    },
}

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rollbar.contrib.django_rest_framework.post_exception_handler',
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_filters.backends.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 25,
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'
if not DEBUG:
    STATIC_URL = 'https://s3.amazonaws.com/assets.bounties.network/' + ENVIRONMENT + '/'
QUEUE_URL = os.environ.get('queue_url', 'https://sqs.us-east-1.amazonaws.com/802922962628/bounties_development.fifo')
NOTIFICATIONS_URL = os.environ.get('notifications_url', 'https://sqs.us-east-1.amazonaws.com/802922962628/notifications_development.fifo')
SLACK_TOKEN = os.environ.get('slack_token')
REDIS_LOCATION = os.environ.get('redis_location', 'redis://127.0.0.1:6379')
LOCAL = os.environ.get('local') == 'true'
ETH_NETWORK = os.environ.get('eth_network', 'mainNet')
DEPLOY_URL = os.environ.get('deploy_url', 'http://127.0.0.1')

networks = {
    'mainNet': 'https://mainnet.infura.io/',
    'rinkeby':  'https://rinkeby.infura.io/',
    'consensysrinkeby':  'https://rinkeby.infura.io/',
    'stagingRinkeby': 'https://rinkeby.infura.io/',
    'localhost': 'localhost:8545',
}

ETH_NETWORK_URL = networks[ETH_NETWORK]
SESSION_COOKIE_HTTPONLY = True
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

NOTIFICATIONS_SLACK_CHANNEL = '#bounty_notifs' if ENVIRONMENT == 'production' else ENVIRONMENT + '_bounty_notifs'

PLATFORM_MAPPING = {
    'colorado': 'https://colorado.bounties.network',
    'consensys': 'https://consensys.bounties.network',
    'hiring': 'https://hiring.bounties.network',
}

if not DEBUG and ENVIRONMENT != 'local':
    SESSION_COOKIE_DOMAIN = '.bounties.network'
