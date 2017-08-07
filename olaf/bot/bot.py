#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apiai
import json

import logging

from olaf.config import Config
from olaf.bot.features import Calculator, Day, Hour, OlafCalendar, Weather, Wikipedia

class Bot:

  ACTIONS_NAME = ["weather", "calendar", "hour", "calculator", "wikipedia", "day"]

  logger = logging.getLogger('olaf-voice.bot')

  def __init__(self):
    self.config = Config()
    self.ai = apiai.ApiAI(self.config.apiai_key)
    self.lang = self.config.lang

    self.functs = {
      self.ACTIONS_NAME[0]: Weather(),
      self.ACTIONS_NAME[1]: OlafCalendar(),
      self.ACTIONS_NAME[2]: Hour(),
      self.ACTIONS_NAME[3]: Calculator(),
      self.ACTIONS_NAME[4]: Wikipedia(),
      self.ACTIONS_NAME[5]: Day()
    }

  def request(self, query):
    request = self.ai.text_request()
    request.lang = self.lang

    request.query = query

    response = json.loads(request.getresponse().read())

    self.logger.debug("[request] API.AI result : %s", response)

    speech = ""

    try:
      speech = self.parse(response)
      self.logger.debug("[request] result : %s", speech)
    except Exception as e:
      self.logger.exception("[request] technical error on parsing")

    return speech

  def parse(self, response):
    speech = "Désolé, je n'ai pas pu traiter ta requete"

    if (response != None):
      result = response.get("result")

      if (result != None):
        action = result.get("action")

        if (self.actionNameDefine(action)):
          context = self.getContext(result, action)

          if (context != None):
            speech = self.executeAction(context)
          else:
            speech = result.get("fulfillment").get("speech").encode("utf8")
        else:
          speech = result.get("fulfillment").get("speech").encode("utf8")

    return speech

  def getContext(self, result, action):
    context = None

    contexts = result.get("contexts")

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

  def executeAction(self, context):
    speech = "Désolé, je ne sais pas encore traiter cette requete"

    funct = self.functs.get(context.get("name"))

    if (funct != None):
      speech = funct.proceed(context)

    return speech