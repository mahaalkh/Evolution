import os, sys
import json
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../'))
from processing import parse_json

def xsilly_tester(confiChoi):
  play, lolos1, lolos2 = parse_json.parse_choice(confiChoi)
  result = play.choose(lolos1, lolos2)
  return json.dumps(result)
