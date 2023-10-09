"""
Django settings for Credibility_verification_system project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
# settings.py

import certifi

# Use certifi to provide trusted certificate authorities
REQUESTS_CA_BUNDLE = certifi.where()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_zazxc)^d4#$$*o_mpshd83wcyid+d01rxowev9htaky251m#&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'jazzmin',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #own
    'users.apps.PagesConfig',
    'crispy_forms',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'users.custom_middleware.SessionTimerMiddleware', 
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Credibility_verification_system.urls'

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

WSGI_APPLICATION = 'Credibility_verification_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD':'dfNdAbfWcGY7aTSm',
        'HOST':'db.tgpyjmiogymsgdcoipbb.supabase.co',
        'PORT':'5432',
        
    }
}


# Email Backend Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Replace with your preferred backend

EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email host
EMAIL_PORT = 587  # Replace with your email port
EMAIL_USE_TLS = True  # Set to False if your email server doesn't use TLS
EMAIL_HOST_USER = 'derricknyaga007@gmail.com'  # Replace with your email username
EMAIL_HOST_PASSWORD = 'ydilhiqbjgoesubj'  # Replace with your email password



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'




CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/statement/'

LOGIN_URL = 'login'

#supabase
SUPABASE_URL = 'https://azprsjaqrtspexqzkwvr.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF6cHJzamFxcnRzcGV4cXprd3ZyIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ0Mjg0NDEsImV4cCI6MjAxMDAwNDQ0MX0.AImB5InnNSfJFk3CkhwTVWsDEEn5h6BsuoKPHnjw-x0'

#LOGIN_URL = 'two_factor:login'

# this one is optional
# LOGIN_REDIRECT_URL = 'two_factor:profile'


#jazzmine
JAZZMIN_UI_TWEAKS = {
    
    "theme": "darkly",
    "dark_mode_theme": "cyborg",
}

JAZZMIN_SETTINGS = {
     "site_title": "Admin Panel",
     
     "site_header": "Admin Panel",
     
     
    "site_logo": "images/logo3.png",
    
    "site_brand": "CVS",
    
     "icons": {
        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-users",
        "Users.users": "fas fa-user"
        
    },
     "show_ui_builder": False,
    
 
}

#session 

SESSION_TIMER = 600