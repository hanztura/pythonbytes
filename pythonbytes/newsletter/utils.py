import json

from django.core.mail import EmailMultiAlternatives
from django.forms import modelformset_factory

from .forms import DeliveryModelForm, Delivery


def send_newsletter(newsletter, subscribers):
    # data
    subject = newsletter.subject
    to = [sub.email_address for sub in subscribers]
    body = newsletter.body
    recipient_variables = {}
    deliveries_data = []  # for saving Delivery instance later
    for subscriber in subscribers:
        email_address = subscriber.email_address
        pk = subscriber.pk
        recipient_variables[email_address] = {'id': str(pk)}

        data = {
            'newsletter': newsletter,
            'subscriber': subscriber,
            'is_success': True
        }
        deliveries_data.append(Delivery(**data))

    recipient_variables = json.dumps(recipient_variables)

    # send email
    msg = EmailMultiAlternatives(subject, body, to=to)
    msg.content_subtype = "html"
    msg.esp_extra = {'recipient-variables': recipient_variables}
    is_success = msg.send()

    if is_success:
        deliveries = Delivery.objects.bulk_create(deliveries_data)

    return is_success
