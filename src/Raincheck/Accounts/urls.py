from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # existing patterns here...
    (r'login/$',  login, {'template_name': 'login.html'}),
    (r'logout/$', logout),
    (r'new_account/$', 'Accounts.views.create_account'),
    (r'profile/$', "Raincheck.Accounts.views.profile"),
    (r'connect_fb/$', "Raincheck.Accounts.views.connect_fb"),
    (r'connect_gcal/$', "Raincheck.Accounts.views.connect_gcal"),
    (r'connect_fbfriends/$', "Raincheck.Accounts.views.connect_fbfriends"),
    (r'conflict/(?P<event_id>\d+)/?$', "Raincheck.Accounts.views.conflict")
)

