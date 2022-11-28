def commaFormat(number):
      number = str(number)
      if '.' in number:
            fractionalPart = number[number.index('.'):]
            number = number[:number.index('.')]
      else:
            fractionalPart = ''
      
      triplet = ''
      commaNumber = ''

      for i in range(len(number) -1, -1,-1):
            triplet = number[i] + triplet
            if len(triplet) == 3:
                  commaNumber = triplet + ',' + commaNumber
                  triplet = ''
      
      if triplet != '':
            commaNumber = triplet + ',' + commaNumber
      return commaNumber[:-1] + fractionalPart

assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'

print('All Assertion Completed!')