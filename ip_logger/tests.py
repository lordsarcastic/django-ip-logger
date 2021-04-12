from time import sleep
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import IPAddress
from .utils import get_ip_address


class MiddlewareTestCase(TestCase):
    def ping(self):
        url = reverse('ipaddr:index')
        return self.client.get(url)

    def test_new_ip_will_be_saved(self):
        response = self.ping()
        request = response.wsgi_request
        ip = get_ip_address(request)
        newly_saved_ip = IPAddress.objects.get(ip=ip)
        self.assertEqual(newly_saved_ip.init_visit, newly_saved_ip.last_visit)

    def test_already_logged_ip_will_change_last_visit(self):
        self.ping()
        # simulate another visit by same address
        sleep(2)
        response = self.ping()
        request = response.wsgi_request
        ip = get_ip_address(request)
        logged_ip = IPAddress.objects.get(ip=ip)
        self.assertNotEqual(logged_ip.init_visit, logged_ip.last_visit)
