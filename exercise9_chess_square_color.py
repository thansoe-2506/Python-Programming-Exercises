def getChessSquareColor(row,col):
      if row > 8 or col > 8 or row < 1 or col < 1:
            return ''
      elif row%2 == 0 and col%2 == 0:
            return 'white'
      elif row%2 == 1 and col%2 == 1:
            return 'white'
      elif row%2 == 1 or col%2 == 1:
            return 'black'
            
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''
print('Assertion Completed!')