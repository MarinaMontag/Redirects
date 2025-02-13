import sys

from .base import *

INSTALLED_APPS += [
    'django_extensions',
    'apps.accounts',
    'corsheaders',
    'rest_framework',
    'drf_spectacular',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

AUTH_USER_MODEL = 'accounts.User'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Environment
TESTING_ENVIRONMENT = 'testing'
PRODUCTION_ENVIRONMENT = 'production'
STAGING_ENVIRONMENT = 'staging'
DEVELOPMENT_ENVIRONMENT = 'development'

if 'test' in sys.argv:
    ENVIRONMENT = TESTING_ENVIRONMENT
else:
    ENVIRONMENT = env('ENVIRONMENT')

# Testing environment optimizations
if ENVIRONMENT == TESTING_ENVIRONMENT:
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]

# CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/?.*$'

# Swagger
SPECTACULAR_SETTINGS = {
    'TITLE': 'Snippets API',
    'DESCRIPTION': 'Test description',
    'VERSION': 'v1',
    'SERVE_INCLUDE_SCHEMA': False,
    'CONTACT': {'email': 'contact@snippets.local'},
    'LICENSE': {'name': 'BSD License'},
    # OTHER SETTINGS
}
