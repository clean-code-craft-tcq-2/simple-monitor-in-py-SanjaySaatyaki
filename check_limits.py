battery_params_range = {
  'temperature' : {'min':0,'max':45,'tolerance':5},
  'soc' : {'min':20,'max':80,'tolerance':5},
  'charge_rate' : {'min':0,'max':0.8,'tolerance':5}
}

battery_state = {0:"NORMAL",1:"LOW LEVEL",2:"HIGH LEVEL"}

languages = {
  'EN' :{'temperature':'Temperature',
          'soc':'State of Charge',
          'charge_rate':'Charge Rate',
          'NORMAL':'NORMAL',
          'LOW LEVEL BREACHED':'LOW LEVEL BREACHED',
          'HIGH LEVEL BREACHED':'HIGH LEVEL BREACHED',
          'LOW LEVEL WARNING':'LOW LEVEL WARNING',
          'HIGH LEVEL WARNING':'HIGH LEVEL WARNING'},
  'DE':{'temperature':'Temperatur',
        'soc':'Ladezustand',
        'charge_rate':'Ladestrom',
        '1':'Limit erreicht',
        '2':'Warnung',
        'NORMAL':'NORMAL',
        'LOW LEVEL BREACHED':'NIEDRIGES NIVEAU ERREICHT',
        'HIGH LEVEL BREACHED': 'HOHES LEVEL ERREICHT',
        'LOW LEVEL WARNING':'NIEDRIGES NIVEAU Warnung',
        'HIGH LEVEL WARNING': 'HOHES LEVEL Warnung',
  }

}


def convert_to_language(params,language):
  string = ''
  for param in params:
    string = string+ "\t"+languages[language][param]  
  return string.strip()

def display_param_status(battery_params,enable_warning,language):
  for param in battery_params:
    params = []
    params.append(param)
    
    param_keys = battery_params[param].keys()
    for key in param_keys:
      key_status = battery_params[param][key]
    if (battery_params[param][key] is not battery_state[0]):
      if key == 'limit_status':
        key_status = key_status + ' BREACHED'
      else:
        key_status = key_status + ' WARNING'
    params.append(key_status)
    
    print(convert_to_language(params,language))

def get_limit(value,min_value):
  if value < min_value:
    return battery_state[1]
  return battery_state[2]

def get_range(value, min_value, max_value):
  if value > min_value and value < max_value:
    return battery_state[0]
  else:
    return get_limit(value,min_value)

def battery_param_status(params,enable_warning,lang):
  battery_params = {}
  for param in params:
    temp ={}
    temp['limit_status'] = get_range(params[param],battery_params_range[param]['min'],battery_params_range[param]['max'])
    if enable_warning:
      tolerance = (battery_params_range[param]['max']*battery_params_range[param]['tolerance'])/100
      temp['warning_status'] = get_range(params[param],battery_params_range[param]['min']+tolerance,battery_params_range[param]['max']-tolerance)
    battery_params[param] = temp
  display_param_status(battery_params,enable_warning,lang)
  return battery_params
      
if __name__ == '__main__':
  battery_param_status({'temperature':25,'soc':70,'charge_rate':0.1},True,"EN")
  battery_param_status({'temperature':50,'soc':85,'charge_rate':0},True,"DE")
  # assert(battery_is_ok(25, 70, 0.7) is True)
  # assert(battery_is_ok(50, 85, 0) is False)
  
