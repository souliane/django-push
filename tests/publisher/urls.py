from django.urls import include, path, re_path

from .feeds import HubFeed, OverrideHubFeed, DynamicHubFeed


urlpatterns = [
    path('feed/', HubFeed(), name='feed'),
    path('override-feed/', OverrideHubFeed(), name='override-feed'),
    path('dynamic-feed/', DynamicHubFeed(), name='dynamic-feed'),
    re_path(r'^subscriber/', include('django_push.subscriber.urls')),
]
