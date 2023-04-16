# import time
# print(time.time())  # timestamp: # of seconds from 1970-01-01 until today (UTC)


# import datetime
# ddate = datetime.datetime(2023, 2, 9)
# print(ddate)


from datetime import datetime

print(datetime(2023, 9, 29))
now = datetime.now()
print(now)

# With directives: https://docs.python.org/3/library/datetime.html
str_date = datetime.strptime("2023-08-15", "%Y-%m-%d")
print(str_date)
print(str_date.strftime("%Y-%m"))

date1 = datetime(1954, 9, 29)
date2 = datetime(1962, 9, 1)
print(date1 > date2)

print(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second,
    now.microsecond
)
