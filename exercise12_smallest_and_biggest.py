def getSmallest(numbers):
      if len(numbers) == 0:
            return None
      # at first I didn't know, this two lines is not necessary
      # if len(numbers) == 1:
      #       return numbers[0]

      minValue = numbers[0]

      for i in numbers[1:]:
            if i < minValue:
                  minValue = i

      return minValue

def getBiggest(numbers):
      if len(numbers) == 0:
            return None
      # if len(numbers) == 1:
      #       return numbers[0]

      maxValue = numbers[0]
      for i in numbers[1:]:
            if i > maxValue:
                  maxValue = i

      return maxValue

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

assert getBiggest([3, 5, 36, 7]) == 36
assert getBiggest([2, 13, 3]) == 13
assert getBiggest([]) == None
assert getBiggest([69]) == 69

print('Assertion Completed!')