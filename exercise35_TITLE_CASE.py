import exercise34_get_upper_case as getUppercase
import random
from tqdm import tqdm
from time import sleep
def getTitleCase(text):
      titlecase = ''
      
      for i in range(len(text)):
            if i == 0:
                  titlecase += getUppercase.getUppercase(text[0])
            elif text[i].isalpha() and not text[i-1].isalpha():
                  titlecase += getUppercase.getUppercase(text[i])
            else:
                  titlecase += text[i].lower()
      
      return titlecase

assert getTitleCase('Hello, world!') == 'Hello, World!'
assert getTitleCase('HELLO') == 'Hello'
assert getTitleCase('hello') == 'Hello'
assert getTitleCase('hElLo') == 'Hello'
assert getTitleCase('') == ''
assert getTitleCase('abc123xyz') == 'Abc123Xyz'
assert getTitleCase('cat dog RAT') == 'Cat Dog Rat'
assert getTitleCase('cat,dog,RAT') == 'Cat,Dog,Rat'

import random
random.seed(42)
chars = list('abcdefghijklmnopqrstuvwxyz1234567890 ,.')
for i in tqdm(range(100), desc = 'Assertion'):
      random.shuffle(chars)
      assert getTitleCase(''.join(chars)) == ''.join(chars).title()
      sleep(0.001)

print('All Assertion Completed!')

