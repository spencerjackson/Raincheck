from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext

def index(request):
	return render_to_response('index.html', {}, context_instance=RequestContext(request))
