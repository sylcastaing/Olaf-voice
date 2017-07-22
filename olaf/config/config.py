#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Config:

  def __init__(self):
    self.test = "aze"

  @property
  def apiai_key(self):
    return self.getConfigFile()['keys']['APIAI']

  @property
  def apiweather_key(self):
    return self.getConfigFile()['keys']['weather']

  @property
  def lang(self):
    return self.getConfigFile()['params']['lang']

  @property
  def city(self):
    return self.getConfigFile()['params']['city']

  def getConfigFile(self):
    with open('./config.json') as data:
      return json.load(data)