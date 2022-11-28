'''
def drawBorder(width,height):
      if width < 2 or height < 2:
            pass
      for i in range(height):
            if i == 0 or i == height-1:
                  print('+',end='')
            else:
                  print('|',end='')
            for j in range(width-1):
                  if j == width-2:
                        if (0<i<height-1):
                              print('|',end='')
                        else:
                              print('+',end='')
                  elif (0<i<height-1):
                        print(' ',end='')
                  else:
                        print('-',end='')
            print()
'''            
def drawBorder(width, height):
    # Special case: If the width or height is less than two, draw nothing:
    if width < 2 or height < 2:
        return

    # Print the top row:
    print('+' + ('-' * (width - 2)) + '+')

    # Loop for each row (except the top and bottom):
    for i in range(height - 2):
        # Print the sides:
        print('|' + (' ' * (width - 2)) + '|')

    # Print the bottom row:
    print('+' + ('-' * (width - 2)) + '+')

drawBorder(16, 4)
drawBorder(4, 8)
drawBorder(3, 3)
drawBorder(2, 2)
drawBorder(20, 8)