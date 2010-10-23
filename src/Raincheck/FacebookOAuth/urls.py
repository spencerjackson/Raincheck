from django.conf.urls.defaults import *

urlpatterns = patterns('',    
    (r'FBOAuth/$', 'Raincheck.FacebookOAuth.views.auth'),
    (r'FBOAuth/dance/?', 'Raincheck.FacebookOAuth.views.dance'),
)
