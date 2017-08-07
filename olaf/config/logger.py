#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import graypy

from olaf.config import Config

class Logger:

  def __init__(self):
    logConfig = Config().getConfigFile()["logger"]

    logger = logging.getLogger()
    logging.basicConfig(format='%(levelname)s:%(message)s')
    logger.setLevel(logConfig["level"])
    logger.addHandler(graypy.GELFHandler(logConfig["host"], logConfig["port"]))