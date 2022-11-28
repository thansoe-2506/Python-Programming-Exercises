def average(numbers):
      total = 0
      size = len(numbers)
      for i in numbers: total += i
      return total/size

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
      random.shuffle(testData)
      assert average(testData) == 2

print('Assertion Completed!')
      