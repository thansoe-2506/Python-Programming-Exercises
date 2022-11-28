def drawPyramid(height):
      for rows in range(height):
            for spaces in range(height-(rows+1)):
                  print(' ',end='')
            for hashs in range(rows+(rows+1)):
                  print('#',end='')
            print()

drawPyramid(8)