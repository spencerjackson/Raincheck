from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from Raincheck import google, facebook
from django.contrib.auth.decorators import login_required
from Raincheck.Events.models import *
import datetime
import random, json
from django.contrib import auth

def normalize(date):
    if not isinstance(date, str): return date
    d,t = date.split("T"); t = t.split("+")[0]
    return datetime.datetime(*[int(i) for i in d.split("-")+t.split(":")])

def conflicts(events, avoid):
    start,end = normalize(avoid["start_time"]), normalize(avoid["end_time"])    
    mid = start+(end-start)/2
    half = mid - start
    list = []
    for event in events:
        s,e = normalize(event["start_time"]), normalize(event["end_time"])
        m = s+(e-s)/2
        h,dur = m-s,e-s
        if (s <= start and e-start >= half) or (s <= mid and e >= end) or (s >= start and e <= end and dur >= half): list.append(event)
    return list

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

def convert_event(event):
    return {"name":event.title, "start_time":event.start_time, "end_time":event.end_time, "event":event}

def date_to_json(date):
    return "new Date(%s, %s, %s, %s, %s, %s)"%(date.year, date.month, date.day, date.hour, date.minute, date.second)

def conflict(request, event_id):
    events = [convert_event(e) for e in Event.objects.filter(creator = request.user)]
    avoid = convert_event(Event.objects.get(id=event_id))
    conflist = conflicts(events, avoid)
    if avoid in conflist:
        conflist.remove(avoid)
    for event in conflist:
        event["start_time"] = date_to_json(event["start_time"])
        event["end_time"] = date_to_json(event["end_time"])
        del event["event"]
    return HttpResponse(json.dumps(conflist))

@login_required
def profile(request):
    #print dir(request.user)
    events = Event.objects.filter(creator = request.user)
    return render_to_response('profile.html', {"session": request.session, "events":events}, context_instance=RequestContext(request))


def create_account(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST['username'], password=request.POST['password2'], email=request.POST['email'])
        user.save()
        
        #auth.login(request, user)    
        return HttpResponseRedirect('/account/profile')
    return render_to_response('new_account.html', {}, context_instance=RequestContext(request))
