#!/usr/bin/env python
# -*- coding: utf-8 -*-

from olaf.config.config import Config
from olaf.bot.bot import Bot

def main():
    monBot = Bot()
    #print monBot.request(sys.argv[1].encode("utf8"))
    print monBot.request("Quel heure est-il ?")
    print monBot.request("Je t'aime")
    print monBot.request("Combien font 1 plus 1 ?")
    print monBot.request("Quel est le récultat de 100 divisé par 10 ?")
    print monBot.request("Combien fait 30 moins 5 ?")
    print monBot.request("Combien fait 20 fois 5 ?")

if __name__ == '__main__':
    main()