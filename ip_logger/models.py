from django.db import models


class IPAddress(models.Model):
    ip = models.GenericIPAddressField(unique=True, verbose_name="IP Address")
    init_visit = models.DateTimeField(null=True, verbose_name="Initial visit")
    last_visit = models.DateTimeField(null=True, verbose_name="Most recent visit")

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "IP address"
        verbose_name_plural = "IP addresses"

