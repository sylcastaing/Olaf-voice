#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class Hour:

  def proceed(self, context):
    now = datetime.datetime.now()
    return "Il est " + str(now.hour) + " h " + str(now.minute)