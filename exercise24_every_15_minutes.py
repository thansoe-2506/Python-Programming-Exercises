minutes_15 = ['00','15','30','45']
hours = ['12','1','2','3','4','5','6','7','8','9','10','11']

for meridiem in ['am','pm']:
      for i in hours:
            for j in minutes_15:
                  print(i+':'+j+meridiem)