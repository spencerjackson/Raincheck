from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

from Raincheck.Excuses.models import Excuse

def index(request):
	excuses = Excuse.objects.all()[:5]
	return render_to_response('index.html', {'excuses': excuses}, context_instance=RequestContext(request))
