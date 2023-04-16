from datetime import datetime, timedelta

# date1 = datetime(2023, 1, 1)
# date2 = datetime(2023, 2, 1)

# delta = date2 - date1
# print(delta)
# print("Days: ", delta.days)
# print("Seconds: ", delta.seconds)
# print("Microseconds: ", delta.microseconds)
# print("Total_seconds: ", delta.total_seconds())


date1 = datetime(2023, 1, 1) + timedelta(weeks=1)
date2 = datetime(2023, 2, 1)

delta = date2 - date1
print(delta)
print("Days: ", delta.days)
print("Seconds: ", delta.seconds)
print("Microseconds: ", delta.microseconds)
print("Total_seconds: ", delta.total_seconds())
