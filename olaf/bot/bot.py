#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apiai
import json

from config.config import Config
from weather import Weather

class Bot:

  def __init__(self):
    self.config = Config()
    self.ai = apiai.ApiAI(self.config.apiai_key)
    self.lang = self.config.lang

    self.weather = Weather()

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
    contexts = result["contexts"]

    if (len(contexts) > 0):
      context = contexts[0]

    return context

  def parseContext(self, context):
    speech = "Désolé, je ne sais pas encore traiter cette requete"

    name = context["name"]

    if (name == "weather"):
      speech = self.weather.getWeather(context)

    return speech