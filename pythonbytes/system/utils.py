import requests

from django.conf import settings


def verify_captcha(captcha):
    """
    captcha is the response from user end
    """
    verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': captcha,
    }

    response = requests.post(
        verify_url,
        params=data)
    response_content = response.json()

    return response_content
