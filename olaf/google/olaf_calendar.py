#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import datetime

from credentials import Credentials
from olaf.config.config import Config
from apiclient import discovery

class OlafCalendar:

  def __init__(self):
    self.config = Config()
    self.days = self.config.days

  def proceed(self, context):
    speech = ""
    parameters = context["parameters"]

    day = parameters["date-time"]
    dateTimeText = parameters["date-time.original"].encode("utf8")
    events = self.callCalendarAPI(day)

    if (events == None or len(events) == 0):
      if (day != None and day != ""):
        speech = "Il n'y a aucun événement de programmé " + dateTimeText
      else:
        speech = "Aucun événement n'est programmé pour les 5 prochains jours"
    
    else:
      speech = "Il y a " + str(len(events)) + " événements à venir "

      showDay = True
      if (day != None and day != ""):
        speech += dateTimeText
        showDay = False
      
      speech += ", : "

      for event in events:
        speech += self.getEventDisplay(event, showDay) + ", "

    return speech

  def callCalendarAPI(self, day):
    g_credentials = Credentials()
    creds = g_credentials.get_credentials()
    http = creds.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    if (day != None and day != ""):
      timeMin = datetime.datetime.strptime(day, "%Y-%m-%d")
      timeMax = timeMin +  datetime.timedelta(days=1)
    else:
      timeMin = datetime.datetime.utcnow()
      timeMax = timeMin + datetime.timedelta(days=5)

    eventsResult = service.events().list(
        calendarId='primary', timeMin=timeMin.isoformat() + 'Z', timeMax=timeMax.isoformat() + 'Z', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    return events

  def getEventDisplay(self, event, showDay):

    eventName = event["summary"].encode("utf-8")  + " "

    dateTime = datetime.datetime.strptime(event["start"]["dateTime"][0:16], "%Y-%m-%dT%H:%M")
    if (showDay):
      eventName += self.config.days[dateTime.weekday()].encode("utf8") + " "

    eventName += ", à " + str(dateTime.hour) + " heure"

    if (dateTime.minute > 0):
      eventName += " " + str(dateTime.minute)

    return eventName
