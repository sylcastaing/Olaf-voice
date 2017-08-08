#!/usr/bin/env python
# -*- coding: utf-8 -*-

from olaf.speech import BingSpeechAPI
from olaf.config import Config

import logging

class Speech:
  
  logger = logging.getLogger('olaf-voice.speech.speech')

  def __init__(self):
    self.config = Config()
    self.bing = BingSpeechAPI(key=self.config.bing_key)

  def recognize(self, data):
    text = None

    try:
      text = self.bing.recognize(data, "fr-FR")
    except Exception as e:
      Speech.logger.error(e.message)
    
    return text

  def synthetize(self, data):
    audio = None
    if (data != None and data != ""):
      audio = self.bing.synthesize(data, "fr-FR", "Male")

    return audio