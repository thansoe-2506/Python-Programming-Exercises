def getCostOfCoffee(numberofCoffees, pricePerCoffee):
      totalPrice = 0.0
      cupUntilFreeCoffee = 8
      for i in range(numberofCoffees):
            if cupUntilFreeCoffee == 0:
                  cupUntilFreeCoffee = 8
            else:
                  totalPrice += pricePerCoffee
                  cupUntilFreeCoffee -= 1
      return totalPrice

def getCostOfCoffee2(numC, priceC):
      numFreeC = numC // 9
      numPaidC = numC - numFreeC
      return priceC * numPaidC

assert getCostOfCoffee2(7, 2.50) == 17.50
assert getCostOfCoffee2(8, 2.50) == 20
assert getCostOfCoffee2(9, 2.50) == 20
assert getCostOfCoffee2(10, 2.50) == 22.50
for i in range(1, 4):
      assert getCostOfCoffee2(0, i) == 0
      assert getCostOfCoffee2(8, i) == 8 * i
      assert getCostOfCoffee2(9, i) == 8 * i
      assert getCostOfCoffee2(18, i) == 16 * i
      assert getCostOfCoffee2(19, i) == 17 * i
      assert getCostOfCoffee2(30, i) == 27 * i

print('All Assertion Completed!')