from tqdm import tqdm
from time import sleep
def convertStrToInt(stringNum):
      if stringNum == '0':
            return 0
      integerNum = 0
      
      DIGITS_STR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
'8': 8, '9': 9}
      if stringNum[0] == '-':
            isNegative = True
            stringNum = stringNum[1:]
      else:
            isNegative = False

      for i in range(len(stringNum)):
            digit = DIGITS_STR_TO_INT[stringNum[i]]
            integerNum = (integerNum*10) + digit

      if isNegative:
            return -integerNum
      else:
            return integerNum


for i in tqdm(range(-100,1000), desc="Assertion"):
      assert convertStrToInt(str(i)) == i
      sleep(.000001)

print('All Assertion Completed!')
