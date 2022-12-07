def rot13(text):
      firsthalf = [chr(x) for x in range(65,78)]
      secondhalf = [chr(x) for x in range(78,91)]
      firsthalflower = [chr(x) for x in range(97, 110)]
      secondhalflower = [chr(x) for x in range(110, 123)]
      result = ''
      for i in range(len(text)):
            
            if text[i] in firsthalf:
                  result += secondhalf[firsthalf.index(text[i])]
            elif text[i] in secondhalf:
                  result += firsthalf[secondhalf.index(text[i])]
            elif text[i] in firsthalflower:
                  result += secondhalflower[firsthalflower.index(text[i])]
            elif text[i] in secondhalflower:
                  result += firsthalflower[secondhalflower.index(text[i])]
            else:
                  result += text[i]
      return result

assert rot13('Hello, world!') == 'Uryyb, jbeyq!'
assert rot13('Uryyb, jbeyq!') == 'Hello, world!'
assert rot13(rot13('Hello, world!')) == 'Hello, world!'
assert rot13('abcdefghijklmnopqrstuvwxyz') == 'nopqrstuvwxyzabcdefghijklm'
assert rot13('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'      

print(rot13('blahhhhh??'))