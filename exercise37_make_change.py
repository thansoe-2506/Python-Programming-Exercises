def makeChange(amount):
      quarters, dimes, nickels, pennies = 0, 0, 0, 0
      remainder = 0
      changes = {}
      quarters = amount//25
      remainder = int(amount%25)
      dimes = remainder//10
      remainder = int(remainder%10)
      nickels = remainder//5
      remainder = int(remainder%5)
      pennies = remainder

      if quarters == 0:
            pass
      else:
            changes['quarters'] = quarters
      if dimes == 0:
            pass
      else:
            changes['dimes'] = dimes
      if nickels == 0:
            pass
      elif nickels != 0:
            changes['nickels'] = nickels
      if pennies == 0:
            pass
      else:
            changes['pennies'] = pennies

      return changes


if __name__ == '__main__':
      assert makeChange(30) == {'quarters': 1, 'nickels': 1}
      assert makeChange(10) == {'dimes': 1}
      assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
      assert makeChange(100) == {'quarters': 4}
      assert makeChange(125) == {'quarters': 5}
      print('All Assertion Complete!')