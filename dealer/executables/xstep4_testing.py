import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from dealer import Dealer
from processing import parse_json
from processing import make_json

def executeXstep4(confiXstep):

  process_configuration, process_xstep4 = parse_json.parse_configuration_with_xstep4(confiXstep)
  [lop, watering_hole, loc] = process_configuration
  dealer = Dealer(watering_hole, lop, loc)
  dealer.step4Apply(process_xstep4)
  new_cofiguration = dealer.get_configuration()
  m_json = make_json.MakeJSON()
  output = m_json.make_configuration(new_cofiguration)
  return output
