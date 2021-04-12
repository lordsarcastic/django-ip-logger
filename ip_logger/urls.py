from django.urls import path

from .views import TestView


app_name = 'ipaddr'

urlpatterns = [
    path('', TestView.as_view(), name='index')
]
