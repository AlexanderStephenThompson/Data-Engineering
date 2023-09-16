import datetime #Always start with this. It also may start off greyed out. Though once you call the module, it'll be normal

"""
Useful link: https://www.w3schools.com/python/python_datetime.asp 

date – Larger time units (Month, day, year)
time – Smaller time units (Hour, minute, second, microsecond)
datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
timedelta— Finding the difference between dates and times.

"""

Today = datetime.date.today()
print(Today)
# Or if you just wanted the month or a particular part of the listed info...
Today = datetime.date.today()
print(Today.month)

# To get days of the week
print()
print(Today.weekday()) #Scale of 0 - 6. 0 being Monday and Sunday being 6.
print(Today.isoweekday()) #Scale of 1 - 7. 1 being Monday and Sunday being 7.


Now = datetime.datetime.now()
print()
Right_now = datetime.datetime.today()#Full info
print(Right_now)

#Time Deltas - Finding the difference in time
Wait_one_week = datetime.timedelta(days=7)

def Next_weeks_date():
    print(Today + Wait_one_week)

Next_weeks_date()

Birthday = datetime.date(2019,7,5)

def Until_birthday():
    print(Birthday - Today)

Until_birthday()

# Or...

Until_My_Birthday = Birthday - Today
print(Until_My_Birthday.days)

# Printing as words
print(Today.strftime("%B %d, %Y"))

