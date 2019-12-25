from django.urls import path

from .views import (
    NewsletterDetailView, NewsletterSendRedirectView, NewsletterListView,
    SubscriberCreateView, UnsubscribeView)


app_name = 'newsletter'
urlpatterns = [
    path(
        'unsubscribe/<str:pk>/<str:token>/',
        UnsubscribeView.as_view(),
        name='unsubscribe'),
    path('subscribers/new/', SubscriberCreateView.as_view(), name='subscribe'),

    path(
        '<str:pk>/send-now/',
        NewsletterSendRedirectView.as_view(),
        name='send'),
    path(
        '<str:pk>/',
        NewsletterDetailView.as_view(),
        name='detail'),
    path('', NewsletterListView.as_view(), name='list'),

]
