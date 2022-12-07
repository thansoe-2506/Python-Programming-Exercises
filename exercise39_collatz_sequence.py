import random
from tqdm import tqdm
from time import sleep
def collatz(number):
      collatzsequence = []
      temp = number
      nextvalue = 0
      if number <= 0:
            return []
      else:
            collatzsequence.append(temp)
            while True:
                  if temp == 1:
                        return collatzsequence
                  elif temp % 2 == 0:
                        nextvalue = int(temp/2)
                        collatzsequence.append(nextvalue)
                  else:
                        nextvalue = (3*temp) + 1
                        collatzsequence.append(nextvalue)
                  temp = nextvalue

if __name__ == '__main__':

      assert collatz(0) == []
      assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
      assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
      assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
      assert len(collatz(256)) == 9
      assert len(collatz(257)) == 123
      random.seed(42)
      for i in tqdm(range(1000), desc='Assertion'):
            startingNum = random.randint(1, 10000)
            seq = collatz(startingNum)
            sleep(0.0000001)
      assert seq[0] == startingNum # Make sure it includes the starting number.
      assert seq[-1] == 1 # Make sure the last integer is 1.

      print('All Assertion Complete!')