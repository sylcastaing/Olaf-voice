#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apiai
import json

from olaf.config.config import Config
from weather import Weather
from olaf.google.olaf_calendar import OlafCalendar

class Bot:

  def __init__(self):
    self.config = Config()
    self.ai = apiai.ApiAI(self.config.apiai_key)
    self.lang = self.config.lang

    self.weather = Weather()
    self.calendar = OlafCalendar()

  def request(self, query):
    request = self.ai.text_request()
    request.lang = self.lang

    request.query = query

    response = json.loads(request.getresponse().read())

    return self.parse(response)

  def parse(self, response):
    speech = "Désolé, je n'ai pas pu traiter ta requete"

    if (response != None):
      result = response["result"]

      if (result != None):
        context = self.getContext(result)

        if (context != None):
          speech = self.parseContext(context)
        else:
          speech = result["fulfillment"]["speech"].encode("utf8")
    
    return speech

  def getContext(self, result):
    context = None

    action = result["action"]
    if (action != None and action != "" and (("weather" in action) or ("calendar" in action))):
      contexts = result["contexts"]

      if (len(contexts) > 0):
        context = contexts[0]

    return context

  def parseContext(self, context):
    speech = "Désolé, je ne sais pas encore traiter cette requete"

    name = context["name"]

    if (name == "weather"):
      speech = self.weather.getWeather(context)
    elif (name == "calendar"):
      speech = self.calendar.getCalendar(context)

    return speech