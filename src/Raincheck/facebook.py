'''
Created on Oct 22, 2010

@author: Lee
'''
import urllib
import json
from django.http import HttpResponse, HttpResponseRedirect

def API(namespace, access_token, extra = None):
    extra = "" if not extra else "&"+extra
    url = "https://graph.facebook.com/me/%s?access_token=%s%s"%(namespace, access_token, extra)
    data = urllib.urlopen(url).read()
    return json.loads(data)["data"]

def validate(fn):
    def wrapper(request):
        if not request.session.get("access_token", False):
            return HttpResponseRedirect("/FBOAuth/")
        else:
            return fn(request)
    return wrapper