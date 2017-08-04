#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

class Wikipedia:

  def proceed(self, context):
    return self.callAPI(context["parameters"]["query"])

  def callAPI(self, query):
    speech = "Désolé, mais il m'est impossible d'en savoir plus..."

    url = "https://fr.wikipedia.org/w/api.php?action=opensearch&format=json&search=" + query

    r = requests.get(url)

    if (r.status_code == 200):
      result = json.loads(r.text.encode("utf8"))

      if (len(result[2]) > 0):
        speech = result[2][0].encode("utf8")

    return speech