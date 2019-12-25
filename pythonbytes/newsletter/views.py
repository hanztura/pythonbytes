import json

from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView

from .forms import SubscriberModelForm, ActivatorModel
from .models import Newsletter, Subscriber
from .utils import send_newsletter


class NewsletterListView(ListView):
    model = Newsletter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related('subscribers')
        return queryset


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterSendRedirectView(RedirectView):
    pattern_name = 'newsletter:detail'
    http_method_names = ('post', 'get')

    def post(self, request, *args, **kwargs):
        newsletter = kwargs.get('pk', None)
        newsletter = get_object_or_404(Newsletter, pk=newsletter)
        subscribers = Subscriber.objects.active()

        deliveries = send_newsletter(newsletter, subscribers)
        if deliveries:
            msg = 'Successfully sent newsletters.'
            messages.success(request, msg)
        else:
            msg = 'Something went wrong.'
            messages.warning(request, msg)

        return super().post(request, *args, **kwargs)


class SubscriberCreateView(View):
    http_method_names = ('post',)

    def post(self, request, *args, **kwargs):
        form = SubscriberModelForm(json.loads(request.body.decode('utf-8')))
        data = {
            'data': '',
            'ok': False,
            'errors': {},
        }
        if form.is_valid():
            form.save()
            data['ok'] = True
        else:
            data['errors'] = form.errors

        return JsonResponse(data)


class UnsubscribeView(View):
    http_method_names = ('get',)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '')
        unsubscribe_key = kwargs.get('token', '')
        subscriber = get_object_or_404(
            Subscriber,
            pk=pk,
            unsubscribe_key=unsubscribe_key)

        INACTIVE_STATUS = ActivatorModel.INACTIVE_STATUS
        if subscriber.status != INACTIVE_STATUS:
            subscriber.status = INACTIVE_STATUS
            subscriber.deactivate_date = now()
            subscriber.save()

        msg = 'Hi {}! This is to confirm you\'re unsubsription \
            to our newsletter. Thank you!'
        msg = msg.format(subscriber.possible_name.upper())
        messages.success(request, msg)

        return HttpResponseRedirect('/')
