from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.forms.models import modelformset_factory
from django.template import RequestContext


from Events.models import Event

# Create your views here.
def create(request):
	EventFormSet = modelformset_factory(Event, exclude=('creator', 'provider'))
	if request.method == 'POST':
		formset = EventFormSet(request.POST, request.FILES)
		formset.creator = request.user
		formset.producer = "local"
		if formset.is_valid():
			formset.save()
	else:
		formset = EventFormSet()
	return render_to_response("create.html", { "formset" : formset,
	}, context_instance=RequestContext(request))
