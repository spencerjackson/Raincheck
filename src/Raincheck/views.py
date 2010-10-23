from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from Raincheck.Excuses.models import Excuse

import facebook, google

def index(request):
	paginator = Paginator(Excuse.objects.all(), 25)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	try:
		excuses = paginator.page(page)
	except (EmptyPage, InvalidPage):
		excuses = paginator.page(paginator.num_pages)

	return render_to_response('index.html', {'excuses': excuses}, context_instance=RequestContext(request))

@google.validate()
@facebook.validate()
def testAPI(request):
    fbdata = facebook.API("events", request.session["access_token"], "limit=50")
    for user in facebook.API("friends", request.session["access_token"], "limit=50"):
        print facebook.API(user["id"]+"/events", request.session["access_token"], "limit=50")
    gdata = google.API(request.session["gcalendar"])
    return HttpResponse(str(gdata+fbdata))
