#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bing_speech_api import BingSpeechAPI

from olaf.config.config import Config

class Speech:

  def __init__(self):
    self.config = Config()
    self.bing = BingSpeechAPI(key=self.config.bing_key)

  def recognize(self, data):
    text = None

    try:
      text = self.bing.recognize(data, "fr-FR")
    except Exception as e:
      print(e.message)
    
    return text

  def synthetize(self, data):
    audio = None
    if (data != None and data != ""):
      audio = self.bing.synthesize(data, "fr-FR", "Male")

    return audio