import calendar
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month

print(calendar.month(year, month))
