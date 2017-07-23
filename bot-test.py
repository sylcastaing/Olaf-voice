#!/usr/bin/env python
# -*- coding: utf-8 -*-

from olaf.config.config import Config
from olaf.bot.bot import Bot

def main():
    monBot = Bot()
    #print monBot.request(sys.argv[1].encode("utf8"))
    print monBot.request("Comment tu t'appel ?")
    print monBot.request("Quel temps fait il demain à Bordeaux ?")
    print monBot.request("Et à Paris ?")
    print monBot.request("Qui es le plus beau ?")
if __name__ == '__main__':
    main()