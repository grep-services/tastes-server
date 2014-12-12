"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# auto reload setting - only in development - but not working
"""
import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload

@timer(3)
def change_code_gracefull_reload(sig):
	if autoreload.code_changed():
		uwsgi.reload()
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tdjik7wi9p7^^#2a*@hflj6=k&qbg8&7(rv%3gh5dg3fgmk&k8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by allauth template tags
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",

    # allauth specific context processors
    "allauth.account.context_processors.account",
    # "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # for gis
    'django.contrib.gis',

    # The Django sites framework is required
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
    # ... include the providers you want to enable:
    # 'allauth.socialaccount.providers.facebook',

    # other apps
    'rest_framework',
    'main',
)

REST_FRAMEWORK = {
    # change later the structure to receive certain key implies that the requests are from the right source not outside.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2', => has no attribute 'geo_db_type' error happens.
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'flyingmenu',
        'USER': 'marine1079',
        'PASSWORD': '1735ranger',
        'HOST': 'db-instance.cd8tmalgqn1t.ap-northeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'

POSTGIS_VERSION = (2, 1, 3)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# don't know what it is, anyway for all-auth
SITE_ID = 1

# also all-auth settings
ACCOUNT_AUTHENTICATION_METHOD = "email"	# default by username_email
ACCOUNT_EMAIL_REQUIRED = True		# default by false
ACCOUNT_EMAIL_VERIFICATION = "none"	# default by optional
ACCOUNT_USERNAME_REQUIRED = False	# deafult by true
ACCOUNT_SESSION_REMEMBER = True		# default by None

LOGIN_REDIRECT_URL = '/'

# SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
# SOCIALACCOUNT_AUTO_SIGNUP = False	# default by true
# SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION
# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email', 'publish_stream'],
#         'METHOD': 'js_sdk'  # instead of 'oauth2'
#     }
# }
