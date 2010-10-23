from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from Raincheck.Excuses.models import Excuse

def index(request):
	excuses = Excuse.objects.all()[:5]
	return render_to_response('index.html', {'excuses': excuses}, context_instance=RequestContext(request))

"""
from django.http import HttpResponse, HttpResponseRedirect
import facebook, google

@google.validate
@facebook.validate
def index(request):
    fbdata = facebook.API("events", request.session["access_token"], "limit=50")
    for user in facebook.API("friends", request.session["access_token"], "limit=50"):
        print facebook.API(user["id"]+"/events", request.session["access_token"], "limit=50")
    gdata = google.API(request.session["gcalendar"])
    return HttpResponse(str(gdata+fbdata))
"""