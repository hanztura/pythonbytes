from django import forms
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail

from .models import Contact
from .utils import verify_captcha


class ContactModelForm(forms.ModelForm):
    captcha = forms.CharField(required=True)

    class Meta:
        model = Contact
        fields = [
            'message',
            'email_address',
            'name',
        ]

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        response_content = verify_captcha(captcha)
        if response_content['success']:
            return captcha
        else:
            msg = 'Unable to verify if you are not a robot.'
            raise ValidationError(msg)

    def send_mail(self):
        host = Site.objects.get_current()
        contact_us = self.cleaned_data
        name = contact_us['name']
        email = contact_us['email_address']
        message = contact_us['message']
        subject = 'Contact Us submitted from: {}'.format(host.domain)
        recepient_list = [admin[1] for admin in settings.ADMINS]

        content_name = 'Name: ' + name
        content_email = 'Email: ' + email
        content_message = 'Message: ' + message
        content = "{}'\n'{}'\n'{}".format(
            content_name, content_email, content_message)

        mail = send_mail(
            subject,
            content,
            email,
            recepient_list
        )
        if mail > 0:
            self.instance.admin_notified = True
            self.instance.save()

            return True

        return False
