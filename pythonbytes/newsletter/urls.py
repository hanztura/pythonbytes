from django.urls import path

from .views import (
    NewsletterDetailView, NewsletterSendRedirectView, NewsletterListView)


app_name = 'newsletter'
urlpatterns = [
    path(
        '<str:pk>/send-now/',
        NewsletterSendRedirectView.as_view(),
        name='send'),
    path(
        '<str:pk>/',
        NewsletterDetailView.as_view(),
        name='detail'),
    path('', NewsletterListView.as_view(), name='list')
]
