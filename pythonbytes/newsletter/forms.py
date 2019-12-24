from django.forms import ModelForm, CharField

from .models import Delivery, Subscriber
from system.utils import verify_captcha


class DeliveryModelForm(ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'newsletter',
            'subscriber',
            'is_success'
        ]


class SubscriberModelForm(ModelForm):
    captcha = CharField(required=True)

    class Meta:
        model = Subscriber
        fields = ['name', 'email_address']

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        response_content = verify_captcha(captcha)
        if response_content['success']:
            return captcha
        else:
            msg = 'Unable to verify if you are not a robot.'
            raise ValidationError(msg)
