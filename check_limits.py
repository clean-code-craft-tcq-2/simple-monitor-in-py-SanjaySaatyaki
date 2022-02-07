def isInRange(value, min_value, max_value=None):
  if max_value == None:
    return value > min_value
  if value < min_value or value > max_value:
    return True

def battery_is_ok(temperature, soc, charge_rate):
  if isInRange(temperature,0,45):
    print('Temperature is out of range!')
    return False
  if isInRange(soc,20,80):
    print('State of Charge is out of range!')
    return False
  if not isInRange(charge_rate,0.8):
    print('Charge rate is out of range!')
    return False

  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
