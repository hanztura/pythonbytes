import requests

from django.conf import settings
from django.forms import CharField


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


class CaptchaFormMixin:
    captcha = CharField(required=True)

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        response_content = verify_captcha(captcha)
        if response_content['success']:
            return captcha
        else:
            msg = 'Unable to verify if you are not a robot.'
            raise ValidationError(msg)
