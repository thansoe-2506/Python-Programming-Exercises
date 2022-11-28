def isLeapYear(year):
      if year%400 == 0:
            return True
      elif year%100 == 0:
            return False
      elif year%4 == 0:
            return True
      else:
            return False

if __name__ == "__main__":
      assert isLeapYear(1999) == False
      assert isLeapYear(2000) == True
      assert isLeapYear(2001) == False
      assert isLeapYear(2004) == True
      assert isLeapYear(2100) == False
      assert isLeapYear(2400) == True

      print('All Assertion Completed!')
