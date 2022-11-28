def getHoursMinutesSeconds(secs):
      if secs <= 0:
            return '0s'

      hours = int(secs/3600)
      secs = secs%3600
      minutes = int(secs/60)
      secs = int(secs%60)

      hms = []

      if hours > 0:
            hms.append(str(hours) + 'h')
      if minutes > 0:
            hms.append(str(minutes) + 'm')
      if secs > 0:
            hms.append(str(secs) + 's')

      return ' '.join(hms)

assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661)  == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'

print('Assertion Completed!')