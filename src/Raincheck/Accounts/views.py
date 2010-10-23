from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from Raincheck import google, facebook
from django.contrib.auth.decorators import login_required
from Raincheck.Events.models import *
import datetime
import random

def normalize(date):
    d,t = date.split("T"); t = t.split("+")[0]
    return datetime.datetime(*[int(i) for i in d.split("-")+t.split(":")])

@login_required
@facebook.validate(redirect = "/account/connect_fb/")
def connect_fb(request):
    fbdata = facebook.API("events", request.session["access_token"], "limit=50")
    for e in fbdata:
        event = Event.objects.get_or_create(title = e["name"],
                                            start_time = normalize(e["start_time"]),
                                            end_time = normalize(e["end_time"]),
                                            creator = request.user,
                                            provider = "fb",
                                            description = e["name"],
                                            )[0]
#        event.start_time = normalize(e["start_time"])
#        event.end_time = normalize(e["end_time"])
#        event.title = e["name"]
#        event.creator = request.user
#        event.location = Locations.objects.get_or_create(location = e["location"] if "location" in e else "")[0]
#        event.provider = "fb"
#        event.description = e["name"]
        event.save()
        
    return HttpResponse(fbdata)

@login_required
@facebook.validate(redirect = "/account/connect_fbfriends/")
def connect_fbfriends(request):
    fbdata = facebook.API("friends", request.session["access_token"], "limit=100")[1:]
    random.shuffle(fbdata)
    i = 0
    for e in fbdata:
        events = facebook.API("events", request.session["access_token"], user = e["id"])
        
        for e in events:
            Event.objects.get_or_create(title = e["name"],
                                                start_time = normalize(e["start_time"]),
                                                end_time = normalize(e["end_time"]),
                                                creator = request.user,
                                                provider = "fb-friends",
                                                description = e["name"],
                                                )
        i += 1
        if i > 5: break
        
    return HttpResponse(fbdata)

@login_required
@google.validate(redirect = "/account/connect_gcal/")
def connect_gcal(request):
    gcal = google.API(request.session["gcalendar"])
    for e in gcal:
        event = Event.objects.get_or_create(title = e["name"],
                                            start_time = normalize(e["start_time"]),
                                            end_time = normalize(e["end_time"]),
                                            creator = request.user,
                                            provider = "gcal",
                                            description = e["name"],
                                            )[0]
#        event.start_time = normalize(e["start_time"])
#        event.end_time = normalize(e["end_time"])
#        event.title = e["name"]
#        event.creator = request.user
#        event.location = Locations.objects.get_or_create(location = e["location"] if "location" in e else "")[0]
#        event.provider = "fb"
#        event.description = e["name"]
        event.save()
        
    return HttpResponse(gcal)

@login_required
def profile(request):
    #print dir(request.user)
    events = Event.objects.filter(creator = request.user)
    return render_to_response('profile.html', {"session": request.session, "events":events}, context_instance=RequestContext(request))
