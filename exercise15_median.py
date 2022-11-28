def median(numbers):
      if len(numbers) == 0: return None
      numbers.sort()
      if len(numbers)%2 == 0:
            middleIndex1 = int(len(numbers)/2) 
            middleIndex2 = middleIndex1 - 1
            return ((numbers[middleIndex1] + numbers[middleIndex2])/2)
      else:
            middleIndex = int(len(numbers)/2)
            return numbers[middleIndex]

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
      random.shuffle(testData)
      assert median(testData) == 6

print('Assertion Completed!')
