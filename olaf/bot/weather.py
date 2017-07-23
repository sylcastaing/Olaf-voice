#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import datetime

from olaf.config.config import Config

class Weather:

  def __init__(self):
    self.config = Config()
    self.apiKey = self.config.apiweather_key
    self.lang = self.config.lang
    self.city = self.config.city

  def getWeather(self, context):
    speech = "La météo est indisponible pour les paramètres que tu m'as donné"
    parameters = context["parameters"]

    weather = self.callWeatherAPI(parameters["address"], parameters["date-time"])

    if (weather != None):
      speech = "Voici les prévision météo "

      if (parameters["date-time.original"] != None and parameters["date-time.original"] != ""):
        speech = speech + "pour " + parameters["date-time.original"].encode("utf8") + " "
      
      if (parameters["address.original"] != None and parameters["address.original"] != ""):
        speech += "à " + parameters["address.original"].encode("utf8") + " "

      
      speech = speech + ": " + self.getFullWeather(weather)

    return speech

  def callWeatherAPI(self, city, day):
    weather = None
    
    if (city == None or city == ""):
      city = self.city
    elif(type(city) is dict):
      city = city["city"]
    else:
      city = city

    city = city.encode("utf8")

    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=" + city + "&units=metric&cnt=8&APPID=" + self.apiKey + "&lang=" + self.lang

    r = requests.get(url)

    if (r.status_code == 200):
      result = json.loads(r.text.encode("utf8"))
      if (day == None or day == ""):
        weather = result["list"][0]
      else:
        day = day + " 14:00"
        timestamp = time.mktime(datetime.datetime.strptime(day, "%Y-%m-%d %H:%M").timetuple())
        
        for element in result["list"]:
          if (element["dt"] == timestamp):
            weather = element
            break

    return weather

  def getFullWeather(self, weather):
    return weather["weather"][0]["description"].encode("utf8") + " avec des températures allant de " + str(int(weather["temp"]["min"])) + " à " + str(int(weather["temp"]["max"])) + " degrés"
