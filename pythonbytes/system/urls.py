from django.urls import path

from .views import ContactCreateView

app_name = 'system'
urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
]