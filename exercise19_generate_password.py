import random

UPPER_LETTERS = [chr(x) for x in range(65,91)]
LOWER_LETTERS = [chr(x) for x in range(97,123)]
SPECIAL = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
NUMBERS = [chr(x) for x in range(48, 58)]
ALL_CHARS = list()
ALL_CHARS[:0] = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+'

def generatePassword(length):
      if length < 12: 
            length = 12

      password = []
      password.append(random.choice(UPPER_LETTERS))
      password.append(random.choice(LOWER_LETTERS))
      password.append(random.choice(NUMBERS))
      password.append(random.choice(SPECIAL))

      while len(password) < length:
            password.append(random.choice(ALL_CHARS))
      
      random.shuffle(password)

      return ''.join(password)

assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
      if character in LOWER_LETTERS:
            hasLowercase = True
      if character in UPPER_LETTERS:
            hasUppercase = True
      if character in NUMBERS:
            hasNumber = True
      if character in SPECIAL:
            hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial


print('All Assertion Completed!')
