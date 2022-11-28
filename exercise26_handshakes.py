def printHandshakes(people):
      numberofhandshakes = 0
      for i in range(len(people)):
            for j in range(i+1,len(people)):
                  print(people[i],'shakes hands with',people[j])
                  numberofhandshakes += 1
      return numberofhandshakes

assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

print('All Assertion Completed!')