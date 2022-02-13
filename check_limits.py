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

def display_param_status(battery_params,language):
  for battery_param in battery_params:
    params =[]
    params.append(battery_param)
    params.append(battery_params[battery_param]) 
    print(convert_to_language(params,language))

def get_limit(value,min_value,check):
  if value < min_value:
    return battery_state[1] + check
  return battery_state[2]+ check

def get_range(value, min_value, max_value,check):
  if value > min_value and value < max_value:
    return battery_state[0]
  else:
    return get_limit(value,min_value,check)

def battery_param_status(params,enable_warning,lang):
  battery_params = {}
  for param in params:
    if enable_warning:
      tolerance = (battery_params_range[param]['max']*battery_params_range[param]['tolerance'])/100
      status = get_range(params[param],battery_params_range[param]['min']+tolerance,battery_params_range[param]['max']-tolerance,' WARNING')
    else:
      status = get_range(params[param],battery_params_range[param]['min'],battery_params_range[param]['max'],' BREACHED')
    battery_params[param] = status

  display_param_status(battery_params,lang)
  return battery_params
      
if __name__ == '__main__':
  assert(battery_param_status({'temperature':25,'soc':70,'charge_rate':0.1},True,"EN") == {'temperature': 'NORMAL', 'soc': 'NORMAL', 'charge_rate': 'NORMAL'})
  assert(battery_param_status({'temperature':50,'soc':85,'charge_rate':0},False,"DE") == {'temperature': 'HIGH LEVEL BREACHED', 'soc': 'HIGH LEVEL BREACHED', 'charge_rate': 'HIGH LEVEL BREACHED'})
  
