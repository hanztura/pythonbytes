from base import *

DEBUG = False

RECAPTCHA_PUBLIC_KEY = os.environ.setdefault('PYTHONBYTES_RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.environ.setdefault('PYTHONBYTES_RECAPTCHA_PRIVATE_KEY', '')
