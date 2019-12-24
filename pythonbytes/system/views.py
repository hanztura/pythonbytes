import json

from django.http import JsonResponse
from django.views.generic.base import View

from .forms import ContactModelForm


class ContactCreateView(View):
    http_method_names = ('post', )

    def post(self, request, *args, **kwargs):
        form = ContactModelForm(json.loads(request.body.decode('utf-8')))
        data = {
            'data': '',
            'ok': False,
            'errors': {},
        }
        if form.is_valid():
            form.save()
            form.send_mail()
            data['ok'] = True
        else:
            data['errors'] = form.errors

        return JsonResponse(data)
