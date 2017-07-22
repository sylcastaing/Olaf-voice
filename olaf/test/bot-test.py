#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

DOSSIER_COURRANT = os.path.dirname(os.path.abspath(__file__))
DOSSIER_PARENT = os.path.dirname(DOSSIER_COURRANT)
sys.path.append(DOSSIER_PARENT)

from config.config import Config
from bot.bot import Bot

def main():
    monBot = Bot()
    print monBot.request(sys.argv[1].encode("utf8"))

if __name__ == '__main__':
    main()