def fizzBuzz(upTo):
    # Loop from 1 up to (and including) the upTo parameter:
    for number in range(1, upTo + 1):
        # If the loop number is divisible by 3 and 5, print 'FizzBuzz':
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz', end=' ')
        # Otherwise the loop number is divisible by only 3, print 'Fizz':
        elif number % 3 == 0:
            print('Fizz', end=' ')
        # Otherwise the loop number is divisible by only 5, print 'Buzz':
        elif number % 5 == 0:
            print('Buzz', end=' ')
        # Otherwise, print the loop number:
        else:
            print(number, end=' ')
fizzBuzz(20)