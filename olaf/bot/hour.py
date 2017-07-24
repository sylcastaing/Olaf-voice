import datetime

class Hour:

  def getHour(self):
    now = datetime.datetime.now()
    return "Il est " + str(now.hour) + " h " + str(now.minute)