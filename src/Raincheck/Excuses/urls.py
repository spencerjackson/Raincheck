from django.conf.urls.defaults import *

urlpatterns = patterns('Raincheck.Excuses.views',
 (r'(?P<excuseID>\d+)/(?P<excuse_is_liked>\D+)/$', 'vote'),
 (r'(?P<id>\d+)/?$', 'single'),
 (r'create','create')
)

