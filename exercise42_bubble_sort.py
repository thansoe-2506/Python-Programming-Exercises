import random
from tqdm import tqdm
from time import sleep

def bubbleSort(alist):
      for i in range(len(alist)):
            for j in range(i+1,len(alist)):
                  if alist[i] > alist[j]:
                        temp = alist[i]
                        alist[i] = alist[j]
                        alist[j] = temp
      return alist

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]

mylist = [4, 1, 3, 56, 2, 0, -1, 9, 32, 99, 28]
newlist = mylist.copy()
newlist.sort()

for i in tqdm(range(100), desc='Assertion'):
      assert bubbleSort(mylist) == newlist
      random.shuffle(mylist)
      random.shuffle(newlist)
      newlist.sort()
      sleep(0.0001)

# print(bubbleSort([2,1,4,0,22]))
print('All Assertion Complete!')