from django.contrib import admin

from .models import IPAddress


class IPAdressAdmin(admin.ModelAdmin):
    list_display = ['ip', 'init_visit', 'last_visit']


admin.site.register(IPAddress)
