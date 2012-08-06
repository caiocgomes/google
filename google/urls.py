
from django.conf.urls.defaults import *

urlpatterns = patterns('',
(r'^/?$', 'google.searchengine.views.search'),
)
