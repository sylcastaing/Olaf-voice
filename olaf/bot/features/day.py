#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from olaf.config import Config

class Day:

  def __init__(self):
    self.config = Config()

  def proceed(self, context):

    speech = ""

    parameters = context["parameters"]

    if (parameters["date"] != None and parameters["date"] != ""):
      date = datetime.datetime.strptime(parameters["date"], "%Y-%m-%d")
      
      if (parameters["date.original"] != None and parameters["date.original"] != ""):
        speech += parameters["date.original"] + ", nous serons le " 
    else:
      date = datetime.datetime.now()
      speech += "Aujourd'hui, nous sommes le "

    speech += self.config.days[date.weekday()].encode("utf8") + " " + str(date.day)

    return speech