from django.http import HttpResponse, HttpResponseRedirect
import facebook, google

@google.validate
@facebook.validate
def index(request):
    fbdata = facebook.API("events", request.session["access_token"], "limit=50")
    gdata = google.API(request.session["gcalendar"])
    return HttpResponse(str(gdata+fbdata))