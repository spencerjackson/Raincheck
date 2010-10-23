# Create your views here.
from Raincheck import google
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def gauth(request):
    if not request.POST.get("gmail", False):
        return render_to_response("gauth/gauth.html")
    guser = request.POST["gmail"]
    gpass = request.POST["password"]
    request.session["guser"] = guser
    request.session["gpass"] = gpass
    calendar = google.GetCalendar(guser, gpass)
    request.session["gcalendar"] = calendar
    return HttpResponseRedirect(request.session.get("redirect_uri", "/"))