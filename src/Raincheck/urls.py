from django.conf.urls.defaults import *
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^FBOAuth/$', 'Raincheck.FacebookOAuth.views.auth'),
    (r'^FBOAuth/dance/?', 'Raincheck.FacebookOAuth.views.dance'),
    
    (r'^/?$', 'Raincheck.views.index'),
    (r'^accounts', include('Raincheck.Accounts.urls')),

    (r'', include('Raincheck.GAuth.urls')),
    #(r'^FBOAuth', include('Raincheck.FacebookOAuth.urls')),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.abspath("./static")}),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
