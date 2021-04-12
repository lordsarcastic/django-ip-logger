from django.utils import timezone

from .models import IPAddress
from .utils import get_ip_address

class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_ip_address(request)
        # log time now to prevent init and last visit
        # from being different even by a second
        now = timezone.now()
        ipaddr, _ = IPAddress.objects.get_or_create(
            ip=ip,
        )
        ipaddr.last_visit = now
        if ipaddr.init_visit is None:
            ipaddr.init_visit = now
        ipaddr.save()
        response = self.get_response(request)
        return response
