import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#ENVIRONMENT = os.environ.get('ENVIRONMENT', default='local')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xr3kd*+gju*+(er3hza5fyh2yyj)w71#)h#eny%i75imd%f2wx'


# Application definitionpip

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #Users allauth
    'django.contrib.sitemaps',

    # 3rd Party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'crispy_forms',
    'ckeditor',
    'django_countries',
    'import_export',
    'sorl.thumbnail',
    'memcache_status',
    'debug_toolbar', 
    'admin_honeypot',
    
    # Apps
    'shop.apps.ShopConfig',
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', 
    
]

ROOT_URLCONF = 'Honeyshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
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

WSGI_APPLICATION = 'Honeyshop.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

from django.utils.translation import gettext_lazy as _
LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
)
#gettext zip instalado
#path /bin instalado C:\Program Files\gettext-utils\bin
#md local
#md local/es && local/en
#django-admin makemessages --all
#agregar tags de traslation
#django-admin compilemessages

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Account & Users
# django-allauth config
AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_REDIRECT_URL = 'shop:home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'shop:home'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

)


ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

DEFAULT_FROM_EMAIL = 'davidalejandrodand@gmail.com'


# STRIPE
STRIPE_TEST_PUBLISHABLE_KEY =  ''
STRIPE_TEST_SECRET_KEY = ''

# EMAIL BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_HOST = 'smtp.sendgrid.net'

# EMAIL_HOST_USER = 'apikey'

# EMAIL_HOST_PASSWORD = ''

# EMAIL_PORT = 587

# EMAIL_USE_TLS = True


# CACHE SETTINGS
#CACHES = {
        #'default': {
            #'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            #'LOCATION': '127.0.0.1:11211',
    #}
#}

#CACHE_MIDDLEWARE_ALIAS = 'default'
#CACHE_MIDDLEWARE_SECONDS = 604800
#CACHE_MIDDLEWARE_KEY_PREFIX = ''


# django-debug-toolbar
#import socket
#hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
#INTERNAL_IPS = ('127.0.0.1:8000')

# production
#if ENVIRONMENT == 'production':
   #SECURE_BROWSER_XSS_FILTER = True
    #X_FRAME_OPTIONS = 'DENY'
    #SECURE_SSL_REDIRECT = True
    #SECURE_HSTS_SECONDS = 3600 
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
    #SECURE_HSTS_PRELOAD = True 
    #SECURE_CONTENT_TYPE_NOSNIFF = True
    #SESSION_COOKIE_SECURE = True 
    #CSRF_COOKIE_SECURE = True
    #SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')   