import datetime
import calendar
def findDay(date):
	born =datetime.datetime.strptime(date,'%d %m %Y').weekday()
	return (calendar.day_name[born])
date="13 03 1999"
print(findDay(date))