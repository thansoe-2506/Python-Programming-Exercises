import random
from tqdm import tqdm
from time import sleep
def myShuffle(mylist):
      return random.shuffle(mylist)

if __name__ == '__main__':
      thelist = [1, 3, 12, 98, 34, 22, 43, 42, 20, 12, 2, 5, 8]
      for i in tqdm(range(800), desc='Assertion'):
            assert myShuffle(thelist) != thelist
            sleep(0.001)
      print('All Assertion Complete!')
