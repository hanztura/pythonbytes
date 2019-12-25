from base import *

DEBUG = False

RECAPTCHA_PUBLIC_KEY = os.environ.setdefault('PYTHONBYTES_RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.environ.setdefault('PYTHONBYTES_RECAPTCHA_PRIVATE_KEY', '')

ALLOWED_HOSTS = ['thepythonbytes.xofytech.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.set(PYTHONBYTES_DATABASE_NAME, ''),
        'USER': os.environ.set(PYTHONBYTES_DATABASE_USER, ''),
        'PASSWORD': os.environ.set(PYTHONBYTES_DATABASE_PASSWORD, ''),
        'HOST': os.environ.set(PYTHONBYTES_DATABASE_HOST, ''),
        'PORT': os.environ.set(PYTHONBYTES_DATABASE_PORT, ''),
    }
}

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 1
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
