def calculateSum(numbers):
      res = 0
      for i in numbers: res += i
      return res

def calculateProduct(numbers):
      res = 1
      for i in numbers: res *= i
      return res

assert calculateSum([]) == 0
assert calculateSum([2, 4, 6, 8, 10]) == 30
assert calculateProduct([]) == 1
assert calculateProduct([2, 4, 6, 8, 10]) == 3840
print('Assertion Completed!')