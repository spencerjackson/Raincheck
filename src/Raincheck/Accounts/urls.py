from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # existing patterns here...
    (r'login/$',  login, {'template_name': 'login.html'}),
    (r'logout/$', logout),
)

