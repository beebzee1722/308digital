"""
Production settings for 308 Digital on GoDaddy hosting
Import from settings.py and override for production
"""

from .settings import *
import os

# Production security settings
DEBUG = False
ALLOWED_HOSTS = ['28h.524.mytemp.website', '*.308digital.com']  # Update with your actual domain

# Secret key from environment variable (MUST be set in cPanel)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-change-this-in-production')

# Database configuration for GoDaddy MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME', '308_digita'),
        'USER': os.environ.get('DB_USER', 'admin_308'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'diGit@l@308_bankSolut!0n'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '3306'),
    }
}

# Static files (CSS, JavaScript, images)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'public_html', 'static')
STATIC_URL = '/static/'

# Media files (user uploads)
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'public_html', 'media')
MEDIA_URL = '/media/'

# Security settings for production
SECURE_SSL_REDIRECT = False  # Set to True when you have HTTPS certificate
SESSION_COOKIE_SECURE = False  # Set to True with HTTPS
CSRF_COOKIE_SECURE = False  # Set to True with HTTPS
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
}

# Allow static files to be served
STATICFILES_DIRS = []

# Logging for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), 'logs', 'django.log'),
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'ERROR',
    },
}
