def drawBox(size):
      if size < 1:
            pass
      # print('  +--+','\n'
      # ' /  /|','\n'
      # '+--+ +','\n'
      # '|  |/','\n'
      # '+--+')
      # Draw back line on top surface:
      print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')

      # Draw top surface:
      for i in range(size):
            print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

      # Draw top line on top surface:
      print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

      # Draw front surface:
      for i in range(size - 1, -1, -1):
            print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

      # Draw bottom lie on front surface:
      print('+' + '-' * (size * 2) + '+')

# In a loop, call drawBox() with arguments 1 to 5:
for i in range(1, 6):
    drawBox(i)
    