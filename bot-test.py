#!/usr/bin/env python
# -*- coding: utf-8 -*-

from olaf.config.config import Config
from olaf.bot.bot import Bot

def main():
    monBot = Bot()
    #print monBot.request(sys.argv[1].encode("utf8"))
    print monBot.request("Quel heure est-il ?")
    print monBot.request("Je t'aime ?")

if __name__ == '__main__':
    main()