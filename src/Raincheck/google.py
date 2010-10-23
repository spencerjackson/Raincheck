import gdata.calendar.service, time
from django.http import HttpResponse, HttpResponseRedirect
import json

def validate(fn):
    def wrapper(request):
        if not request.session.get("guser", False):
            return HttpResponseRedirect("/Gauth/")
        else:
            return fn(request)
    return wrapper

def GetCalendar(username, password):
    calendar_service = gdata.calendar.service.CalendarService()
    calendar_service.email = username
    calendar_service.password = password
    calendar_service.ProgrammaticLogin()
    return calendar_service

def API(calendar):
    feed = calendar.GetCalendarEventFeed()
    #list = [[e.title, "attending", e.when.start_time, e.when.end_time, "g"+e.id] for e in feed.entry]
    list = [{"name":e.title.text, "start_time":e.when[0].start_time+"T00:00:00+0000", "end_time":e.when[0].end_time+"T00:00:00+0000", "rsvp_status":"attending", "id":"g"+e.id.text, "location":"None"} for e in feed.entry]
    return json.loads(json.dumps(list))