from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', view_books),
    url(r'^cache/', view_cached_books),
]