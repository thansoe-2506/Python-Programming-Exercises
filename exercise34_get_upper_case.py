def getUppercase(text):
      upperText = ''
      for i in text:
            if ('a'<=i<='z'):
                  upperText += chr(ord(i)-32)

            else:
                  upperText += i
      # print(upperText)
      return upperText

if __name__ == '__main__':


      assert getUppercase('Hello') == 'HELLO'
      assert getUppercase('hello') == 'HELLO'
      assert getUppercase('HELLO') == 'HELLO'
      assert getUppercase('Hello, world!') == 'HELLO, WORLD!'
      assert getUppercase('goodbye 123!') == 'GOODBYE 123!'
      assert getUppercase('12345') == '12345'
      assert getUppercase('') == ''

      print('All Assertion Completed!')