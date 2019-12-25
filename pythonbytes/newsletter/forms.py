from django.forms import ModelForm, BooleanField, CharField
from django.utils.timezone import now

from django_extensions.db.models import ActivatorModel

from .models import Delivery, Subscriber
from system.utils import verify_captcha, CaptchaFormMixin


class DeliveryModelForm(ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'newsletter',
            'subscriber',
            'is_success'
        ]


class SubscriberModelForm(CaptchaFormMixin, ModelForm):

    class Meta:
        model = Subscriber
        fields = ['name', 'email_address']

    def save(self, commit=True):
        email_address = self.cleaned_data['email_address']

        # check if email already exist in database
        # if existing then update status to active
        subscriber = Subscriber.objects.filter(
            email_address=email_address)
        if subscriber.exists():
            subscriber = subscriber.first()
            ACTIVE_STATUS = ActivatorModel.ACTIVE_STATUS
            if subscriber.status != ACTIVE_STATUS:
                subscriber.status = ACTIVE_STATUS
                subscriber.activate_date = now()
                subscriber.save()

            return subscriber

        return super().save(commit)
