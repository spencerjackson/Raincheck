'''
Created on Oct 22, 2010

@author: Lee
'''
import urllib
import json
from django.http import HttpResponse, HttpResponseRedirect

class FacebookException(Exception):pass

def API(namespace, access_token, extra = None, user = "me"):
    extra = "" if not extra else "&"+extra
    url = "https://graph.facebook.com/%s/%s?access_token=%s%s"%(user,namespace, access_token, extra)
    data = urllib.urlopen(url).read()
    return json.loads(data)["data"]

def validate(redirect = "/"):
    def wrapper2(fn):
        def wrapper(request):
            if not request.session.get("access_token", False):
                request.session["redirect"] = redirect
                return HttpResponseRedirect("/FBOAuth/")
            else:
                try:
                    return fn(request)
                except KeyError:
                    return HttpResponseRedirect("/FBOAuth/")
        return wrapper
    return wrapper2