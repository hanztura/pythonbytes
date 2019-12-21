from django.forms import ModelForm

from .models import Delivery


class DeliveryModelForm(ModelForm):
    class Meta:
        model = Delivery
        fields = [
            'newsletter',
            'subscriber',
            'is_success'
        ]
