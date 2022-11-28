import exercise20_leap_year as leapyear
import datetime

def isValidDate(year, month, day):
      if not (1 <= month <= 12):
            return False
      if leapyear.isLeapYear(year) and month == 2 and day == 29:
            return True
      if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <=31):
            return False
      elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
            return False
      elif month == 2 and not (1 <= day <= 28):
            return False
      
      return True

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False

d = datetime.date(1970, 1, 1)
oneDay = datetime.timedelta(days=1)
for i in range(1000000):
      assert isValidDate(d.year, d.month, d.day) == True
      # print(d.year, d.month, d.day)
      d += oneDay

print('All Assertion Completed!')
