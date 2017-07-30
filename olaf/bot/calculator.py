#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Calculator:

  def __init__(self):
    self.functs = {
      "+": self.add,
      "-": self.subtract,
      "x": self.multiply,
      "/": self.divide
    }

  def proceed(self, context):

    result = "Je n'ai pas pu calculer le résultat"

    parameters = context.get("parameters")
    nb1 = parameters.get("nb1")
    nb2 = parameters.get("nb2")
    operator = parameters.get("operator")

    if (nb1 != None and nb2 != None and operator != None):
      funct = self.functs.get(operator)

      if (funct != None):
        nb1 = int(nb1)
        nb2 = int(nb2)
        result = funct(nb1, nb2)

    return result

  def add(self, nb1, nb2):
    return nb1 + nb2

  def subtract(self, nb1, nb2):
    return nb1 - nb2

  def multiply(self, nb1, nb2):
    return nb1 * nb2

  def divide(self, nb1, nb2):
    return nb1 / nb2