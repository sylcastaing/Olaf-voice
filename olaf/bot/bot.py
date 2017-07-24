#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apiai
import json

from olaf.config.config import Config
from weather import Weather
from hour import Hour
from olaf.google.olaf_calendar import OlafCalendar

class Bot:

  ACTIONS_NAME = ["weather", "calendar", "hour"]

  def __init__(self):
    self.config = Config()
    self.ai = apiai.ApiAI(self.config.apiai_key)
    self.lang = self.config.lang

    self.weather = Weather()
    self.calendar = OlafCalendar()
    self.hour = Hour()

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
        action = result["action"]

        if (self.actionNameDefine(action)):
          context = self.getContext(result, action)

          if (context != None):
            speech = self.parseContext(context)
          else:
            speech = result["fulfillment"]["speech"].encode("utf8")
        else:
          speech = result["fulfillment"]["speech"].encode("utf8")

    return speech

  def getContext(self, result, action):
    context = None

    contexts = result["contexts"]

    for c in contexts:
      if (c["name"] in action):
        context = c
        break

    return context

  def actionNameDefine(self, action):
    define = False

    for name in self.ACTIONS_NAME:
      if (name in action):
        define = True
        break

    return define

  def parseContext(self, context):
    speech = "Désolé, je ne sais pas encore traiter cette requete"

    name = context["name"]
    print(name)
    if (name == "weather"):
      speech = self.weather.getWeather(context)
    elif (name == "calendar"):
      speech = self.calendar.getCalendar(context)
    elif (name == "hour"):
      speech = self.hour.getHour()
    return speech