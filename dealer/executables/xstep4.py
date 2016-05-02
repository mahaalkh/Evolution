import os, sys
import json
import xstep4_testing
this_package_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(this_package_path, '../../'))
from dealer import *
from processing import parse_json
from processing import make_json


def main():
  """
  takes a configuration from stdin and outputs the new_situation after the first step in the feeding
  """

  configStep4 = json.load(sys.stdin)
  output = xstep4_testing.executeXstep4(configStep4)
  print output


main()
