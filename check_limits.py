def isInRange(value, min_value, max_value=None):
  if value > min_value and value < max_value:
    return True
  return False

def isGreaterThanMin(value, min_value):
  if value > min_value:
    return False
  return True

def battery_is_ok(temperature, soc, charge_rate):

  isTemperatureOk = isInRange(temperature,0,45)
  isSocOk = isInRange(soc,20,80)
  isChargeOk = isGreaterThanMin(charge_rate,0.8)

  return isTemperatureOk and isSocOk and isChargeOk


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
