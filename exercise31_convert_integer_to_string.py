from tqdm import tqdm
from time import sleep
def convertIntToStr(integerNum):
      if integerNum == 0:
            return '0'
      stringNum = ''
      DIGITS_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
      if integerNum < 0:
            isNegative = True
            integerNum = abs(integerNum)
      else:
            isNegative = False
      
      while integerNum > 0:
            onesPlaceDigit = integerNum%10
            stringNum = DIGITS_INT_TO_STR[onesPlaceDigit] + stringNum
            integerNum //= 10

      if isNegative:
            return '-' + stringNum
      else:
            return stringNum

for i in tqdm(range(-100, 1000), desc="Assertion"):
      assert convertIntToStr(i) == str(i)
      sleep(.000001)

print('All Assertion Completed!')
