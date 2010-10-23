# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import urllib, urllib2
client_id = "163856460308681"
client_secret = "60ff1ecaeb3312c4a1bce1618251b914"

def auth(request):
    #request.session.flush()
    return HttpResponseRedirect("""https://graph.facebook.com/oauth/authorize?client_id=%s&redirect_uri=http://localhost:8080/FBOAuth/dance/&scope=user_events,friends_events,read_requests"""%client_id)

def dance(request):
    code = request.GET["code"]
    request.session["code"] = code
    url = "https://graph.facebook.com/oauth/access_token?client_id=%s&redirect_uri=http://localhost:8080/FBOAuth/dance/&client_secret=%s&code=%s"%(client_id, client_secret, code)
    data = urllib.urlopen(url).read()
    access_token, expires = [d.split("=")[1] for d in data.split("&")]
    request.session["access_token"] = access_token
    request.session["expires"] = expires
    
    return HttpResponseRedirect(request.session.get("redirect_uri", "/"))