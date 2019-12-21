from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

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
