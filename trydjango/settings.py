"""
Django settings for trydjango project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
# CW: settings.py is central to our project and manages everything.
# -> run 'python manage.py migrate' to sync the settings below with our Django projects and whichever apps we have
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# CW: BASE_DIR is the filepath to my 'src' folder (C:\Users\chris\Documents\Dev\trydjango\src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# CW: The secret should remain private (i.e. do not publicly host settings.py for security of my webapp)
SECRET_KEY = '%et_kmsu50cotpcp&dfl(46d=w4%+q5!p-rj1lznynif*z&pcf'

# SECURITY WARNING: don't run with debug turned on in production!
# CW: Turn off when live and external users will be using the app (want to hide error messages from users)
DEBUG = True
# CW: Domain names that are allowed
ALLOWED_HOSTS = []


# Application definition
# CW: A cornerstone of Django. I will build my app and then put it in installed apps.
INSTALLED_APPS = [
    'django.contrib.admin', # admin user managment area
    'django.contrib.auth', # create user
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party

    # own
    'products',
]
# CW: Contains sutff like requests and how they are handled as well as security. What's cool is that there are already a lot of security features installed.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# CW: URLs are the '/abc' stuck onto your server name. Django manages this automatically (really cool).
ROOT_URLCONF = 'trydjango.urls'
# CW: HTML Pages getting rendered in Django
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
            ],
        },
    },
]
# CW: This is how the server works - it uses this setting
WSGI_APPLICATION = 'trydjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# CW: You can change the name of your backend to point to another database
# -> if you add a new database you just need to change the name of the db in 'NAME', run python manage.py migrate and django will add it for you
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
# CW: Just validates if passwords are good
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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# CW: Internationalization stuff
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# CW: Where you store your static files (images, javascript, css)
STATIC_URL = '/static/'