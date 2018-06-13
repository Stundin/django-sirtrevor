try:  # pre 1.6
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url

from .views import attachment

urlpatterns = [
    url('^attachments/', attachment, name='sirtrevor_attachments'),
]
