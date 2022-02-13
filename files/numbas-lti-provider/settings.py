#######################################################################
# Settings for the Numbas LTI provider
# For help with this file, see
#   https://docs.numbas.org.uk/lti/en/latest/installation/settings.html
#######################################################################

import os
import environ

env = environ.Env(
    DEBUG = (bool, False),
    LOGLEVEL = (str,' WARNING'),
    INSTANCE_NAME = (str, 'Docker'),
    LANGUAGE_CODE = (str, 'en'),
    TIME_ZONE = (str, 'UTC'),
    SUPPORT_NAME = (str, 'the Numbas team'),
    SUPPORT_URL = (str, None),
    EMAIL_COMPLETION_RECEIPTS = (bool, False),
    DEFAULT_FROM_EMAIL = (str,None),
)

# Show debug information when there are errors?
# Set this to False when running in production!
DEBUG = env('DEBUG')

##########################
# Settings that shouldn't change.
# You can ignore these, but they must be present.
##########################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_AUTO_FIELD='django.db.models.AutoField'

SESSION_COOKIE_NAME = 'numbas_lti_provider'

LOGIN_URL = '/login'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'statici18n',
    'huey.contrib.djhuey',
    'numbas_lti',
    'bootstrapform',
    'bootstrap_datepicker_plus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django_auth_lti.middleware_patched.MultiLTILaunchAuthMiddleware',
    'numbas_lti.middleware.NumbasLTIResourceMiddleware',
]

AUTHENTICATION_BACKENDS = ['numbas_lti.backends.LTIAuthBackend','django.contrib.auth.backends.ModelBackend']

ROOT_URLCONF = 'numbasltiprovider.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'numbas_lti.context_processors.global_settings',
            ],
        },
    },
]

ASGI_APPLICATION = 'numbasltiprovider.asgi.application'

# A secret key used for cryptography - this is set by the setup script.
SECRET_KEY = env('SECRET_KEY')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': env('LOGLEVEL').upper(),
    },
}

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']

HUEY = {
	'huey_class': 'huey.PriorityRedisHuey',
    'connection': {
        'host': os.environ.get('REDIS_HOST','redis'),
        'port': int(os.environ.get('REDIS_PORT','6379')),
    },
}

# Password validation
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

LOCALE_PATHS = (os.path.join(BASE_DIR,'locale'),)

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

##############################
# Settings you can change.
##############################

# The name of this instance.
# Shown in the footer of most pages.
INSTANCE_NAME = env('INSTANCE_NAME')

# Which domain names can this server be accessed through?
ALLOWED_HOSTS = [env('SERVERNAME'), '127.0.0.1', 'localhost']

# Which roles should be interpreted as conferring instructor privileges?
LTI_INSTRUCTOR_ROLES = ['Instructor','Administrator','ContentDeveloper','Manager','TeachingAssistant']

# Database connection details
# This is normally set by the setup script.
# See https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'numbas_lti',
        'USER': 'numbas_lti',
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
    }
}

# Channels communication layers.
# This is normally set by the setup script.
# See https://channels.readthedocs.io/en/stable/topics/channel_layers.html
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
                        "hosts": ['redis://' + os.environ.get('REDIS_HOST','redis') + ":" + os.environ.get('REDIS_PORT', '6379')],
        },
    },
}

# The language to use for the interface.
# Available languages: 'en' (English), 'de' (German/Deutsch)
LANGUAGE_CODE = env('LANGUAGE_CODE')

# The time zone that the server should use to display dates and times.
# See https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = env('TIME_ZONE')

# The filesystem path where media files are stored.
MEDIA_ROOT = '/opt/numbas-lti-media/'

# The filesystem path where static files are stored.
STATIC_ROOT = '/opt/numbas-lti-static/'

# The name of your support contact.
SUPPORT_NAME = env('SUPPORT_NAME')

# An address to get support. When there's an error, students will be shown a link to this address.
# Set to "mailto:your_email_address", or the URL of a page containing contact info.
# Or set to None if you don't want to show a link.
SUPPORT_URL = env('SUPPORT_URL')

# Enable sending attempt completion receipts by email?
EMAIL_COMPLETION_RECEIPTS = env('EMAIL_COMPLETION_RECEIPTS')

# The email address to send emails from.
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

# The number of seconds to wait for requests to timeout, such as outcome reports or fetching SCORM packages.
REQUEST_TIMEOUT = 60

# The number of days after creation to keep report files before deleting them.
REPORT_FILE_EXPIRY_DAYS = 30

