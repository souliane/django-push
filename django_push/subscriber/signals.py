import django

from django.dispatch import Signal

if django.get_version().split(".")[0] >= "4":
    updated = Signal()
else:
    updated = Signal(provided_args=['notification', 'request', 'links'])


