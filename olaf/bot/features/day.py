#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging

from olaf.config import Config

class Day:

  logger = logging.getLogger('olaf-voice.bot.day')

  def __init__(self):
    self.config = Config()

  def proceed(self, context):

    speech = ""

    parameters = context["parameters"]

    if (parameters["date"] != None and parameters["date"] != ""):

      Day.logger.debug("[proceed] get day with date parameter")

      date = datetime.datetime.strptime(parameters["date"], "%Y-%m-%d")
      
      if (parameters["date.original"] != None and parameters["date.original"] != ""):
        Day.logger.debug("[proceed] add original date")

        speech += parameters["date.original"].encode("utf8") + ", nous serons le " 
    else:

      Day.logger.debug("[proceed] get today date")

      date = datetime.datetime.now()
      speech += "Aujourd'hui, nous sommes le "

    speech += self.config.days[date.weekday()].encode("utf8") + " " + str(date.day) + " " + self.config.months[date.month - 1].encode("utf8")

    return speech