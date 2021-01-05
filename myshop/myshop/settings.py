"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sfuh5dy_eirgxyok=s+z#i86ee*(%pka^6xe^)@ypv(=er6cig'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'myonlineshop.apps.MyonlineshopConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'account.apps.AccountConfig',
    'payment',
    'blog',
    'coupons.apps.CouponsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'django_countries',
    'social_django',
    'django_extensions',
    'taggit',
    'django.contrib.postgres',
    'currencies',
    'paystack',
    'tawkto',
    'phonenumber_field',
    'ckeditor',
    
    
    
]

if django.VERSION < (1, 7):
    INSTALLED_APPS += (
        'south',
    )


CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'currencies.context_processors.currencies',
               
                # 'myonlineshop.context_processors.category',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mystore',
        'USER': 'postgres',
        'PASSWORD': 'mide',

        
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',



]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '399053652477-t9nrl6apjefq6cahehfc3m0evh7vop4s.apps.googleusercontent.com' # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'RqOy8U5r1j735LDGMcRtm8nH' # Google Consumer Secret


SOCIAL_AUTH_TWITTER_KEY = 'O3mnge5tFjAJzoLf6XIdOCRj4' # Twitter API Key
SOCIAL_AUTH_TWITTER_SECRET = 'moyxjA9efxARarz1c80CK9KRTGDoKvPrUYANNIqKPp7pXKllWm' # Twitter API Secret

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

from django.utils.translation import gettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True 

# SESSION_COOKIE_HTTPONLY = True 

# SECURE_SSL_REDIRECT = True


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'myshop/static')
# ]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'images/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


CART_SESSION_ID = 'cart'


LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.tishman.com.ng'  #Hosted on namecheap Ex: mail.pure.com
EMAIL_USE_TLS = False
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info@tishman.com.ng' 
EMAIL_HOST_PASSWORD = '-5eugAp8K,2u'


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1

OPENEXCHANGERATES_APP_ID = "aaa7cca31d214c8fb05faa97ecc52297"


DEFAULT_CURRENCY = "NGN"

PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'

# PAYSTACK_PUBLIC_KEY='sk_live_64fbaab28d0dbe0d4658a3f36f7a76c0d242ff52'
# PAYSTACK_SECRET_KEY='pk_live_38a49aeb965b4b408380bb775e6ecf83de808e89'
TAWKTO_ID_SITE = '5f8d61defd4ff5477ea706eb'
TAWKTO_API_KEY = '7f6ae4039e325bf900ecd0b9edfd9a4b50bd362a'
# TAWKTO_IS_SECURE = True