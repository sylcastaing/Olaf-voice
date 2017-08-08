#!/usr/bin/env python
# -*- coding: utf-8 -*-
from olaf.config import Logger
from olaf.bot.bot import Bot

def main():
    monBot = Bot()
    Logger()
    #print monBot.request(sys.argv[1].encode("utf8"))
    monBot.request("Quel jour sommes nous ?")
    monBot.request("Quel jour serons nous demain ?")
    monBot.request("Quel jour serons nous le 12 octobre ?")
    #monBot.request("Salut")

if __name__ == '__main__':
    main()