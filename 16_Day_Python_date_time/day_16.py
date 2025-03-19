from datetime import datetime, date

# Getting module functions
print(dir(datetime))

# Getting datetime information
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
# Number of seconds elapsed since 1st of January 1970 UTC
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

# Formatting date output using strftime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
print()

# Using strptime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print()

# date from datetime
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
print()

# Time objects to represent time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
print()

# Difference between two points in time using
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
print()

# Difference between two points in time using timedelata
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
print()

current_now = datetime.now()
print(current_now.day)
print(current_now.month)
print(current_now.year)
print(current_now.hour)
print(current_now.minute)
print(current_now.timestamp)
print()

print(current_now.strftime('%m/%d/%Y, %H:%M:%S'))
print()

today_date = "5 December, 2019"
print(datetime.strptime(today_date, "%d %B, %Y"))
print()

new_year_2024 = datetime(year = 2026, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = new_year_2024 - current_now
print('Difference is: ', diff)

from_epoch = current_now - datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
print('Difference is: ', from_epoch)

new_year_2024 = datetime(year = 2023, month = 5, day = 13, hour = 0, minute = 0, second = 0)
diff = new_year_2024 - current_now
print('Difference is: ', diff)
