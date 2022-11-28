def drawRectangle(width, height):
      if width <=0 or height <=0:
            pass
      for i in range(height):
            for j in range(width):
                  print('# ',end='')
            print()

drawRectangle(10, 10)