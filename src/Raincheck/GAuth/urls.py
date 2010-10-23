from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^Gauth/$', 'Raincheck.GAuth.views.gauth'),
)