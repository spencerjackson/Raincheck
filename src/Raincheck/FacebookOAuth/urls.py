from django.conf.urls.defaults import *

urlpatterns = patterns('',    
    (r'/$', 'Raincheck.FacebookOAuth.views.auth'),
    (r'dance/?', 'Raincheck.FacebookOAuth.views.dance'),
)