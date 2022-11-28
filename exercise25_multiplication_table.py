print('  |  1  2  3  4  5  6  7  8  9 10')
print('--+------------------------------')
for i in range(1,11):
      print(str(i).rjust(2) + '|', end=' ')
      for j in range(1, 11):
            print(str(i*j).rjust(2), end=' ')
      print()